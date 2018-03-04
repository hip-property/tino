import os.path

import yaml
import shlex
import re


class BuildConfig:

    def __init__(self):
        if os.path.exists(".gitlab-ci.yml"):
            with open(".gitlab-ci.yml", 'r') as stream:
                self.config = yaml.load(stream)

    def config_exists(self):
        return self.config is not None

    def get_build_config(self):
        return self.config

    def get_stages(self):
        if self.config_exists():
            return self.config.get("stages")
        else:
            return {}

    def get_variables(self):
        if "variables" not in self.config:
            return {}

        return self.config.get("variables")

    def get_jobs_for_stage(self, stage):
        return {k: v for k, v in self.config.items() if isinstance(v, dict) and v.get("stage") == stage}

    def get_job_config(self, job_name):
        if job_name not in self.config:
            return {}

        return self.config.get(job_name)

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
