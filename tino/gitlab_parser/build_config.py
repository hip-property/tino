import os.path
import re
import shlex

import yaml

GITLAB_BUILD = ".gitlab-ci.yml"
LOCAL_BUILD = ".local-build.yml"


class BuildConfig:

    def __init__(self):
        self.variables = {}
        self.jobs = {}
        self.stages = []

        self.parse_config(GITLAB_BUILD)
        self.parse_config(LOCAL_BUILD)

    def parse_config(self, build_file):
        if os.path.exists(build_file):
            with open(build_file, 'r') as stream:
                _config = yaml.load(stream)

                if "stages" in _config:
                    self.stages = _config.get("stages") + self.stages

                if "variables" in _config:
                    self.variables = {**_config.get("variables"), **self.variables}

                _jobs = {k: v for k, v in _config.items() if isinstance(v, dict) and "stage" in v}
                self.jobs = {**_jobs, **self.jobs}

    def get_stages(self):
        return self.stages

    def get_variables(self):
        return self.variables

    def get_jobs_for_stage(self, stage):
        return {k: v for k, v in self.jobs.items() if v.get("stage") == stage}.keys()

    def get_job_config(self, job_name):
        if job_name not in self.jobs:
            return {}

        return self.jobs.get(job_name)

    def get_job_script_array(self, job_name):
        job_config = self.get_job_config(job_name)

        if "script" not in job_config:
            return {}

        return job_config.get("script")

    def get_job_script_string(self, job_name):
        return ';'.join(self.get_job_script_array(job_name))

    def get_job_variables(self, job_name):
        script_string = self.get_job_script_string(job_name)
        script_words = shlex.split(script_string)

        all_variable_names = []
        for word in script_words:
            variables = re.findall("(\$[{]*[a-zA-Z_]+[}]*)", word)
            variables = map(lambda x: x.replace("$", ""), variables)
            variables = map(lambda x: x.replace("{", ""), variables)
            variables = map(lambda x: x.replace("}", ""), variables)
            all_variable_names.extend(variables)

        assignments = []
        for variable_name in set(all_variable_names):
            if variable_name + "=" in script_string:
                assignments.append(variable_name)

        variable_names = []
        for variable_name in set(all_variable_names):
            if variable_name not in assignments:
                variable_names.append(variable_name)

        return variable_names
