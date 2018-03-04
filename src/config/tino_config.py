import os.path

import yaml

CONFIG_FILENAME = ".gitlab-ci-local-conf.yml"


class TinoConfig:

    def __init__(self):
        if not os.path.exists(CONFIG_FILENAME):
            self.config = {}

        with open(CONFIG_FILENAME, 'r') as stream:
            self.config = yaml.load(stream)

    def get_tino_config(self):
        return self.config

    def get_job_config(self, job_name):
        if job_name not in self.config:
            return {}

        return self.config.get(job_name)

    def get_job_variables(self, job_name):
        job_config = self.get_job_config(job_name)

        if "variables" not in job_config:
            return {}

        return job_config.get("variables")

    def update_job_variables(self, job_name, variables):
        if job_name not in self.config:
            self.config[job_name] = {}

        self.config[job_name]["variables"] = variables

        with open(CONFIG_FILENAME, 'w') as outfile:
            yaml.dump(self.config, outfile, default_flow_style=False)
