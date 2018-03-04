#!/usr/bin/env python
import sys

from config.build_config import BuildConfig
from config.tino_config import TinoConfig
from config.bash_executor import execute_script


def parse_args():
    global job
    if len(sys.argv) != 3:
        exit()
    job = sys.argv[2]


def get_variable_value(variable_name, hardcoded_values, default_values):
    if variable_name in hardcoded_values:
        return hardcoded_values.get(variable_name)
    elif variable_name in default_values:
        input_str = input("Enter [" + variable_name + "] value [" + str(default_values.get(variable_name)) + "]:")
        if not input_str:
            return str(default_values.get(variable_name))
        else:
            return input_str
    else:
        return input("Enter [" + variable_name + "] value:")


def get_script_variable_values():
    variable_names = buildConfig.get_job_variables(job_name=job)
    default_values = tinoConfig.get_job_variables(job_name=job)
    hardcoded_values = buildConfig.get_variables()
    variable_values = {}
    for variable_name in sorted(set(variable_names)):
        variable_values[variable_name] = get_variable_value(variable_name, hardcoded_values, default_values)

    return variable_values


parse_args()
buildConfig = BuildConfig()
tinoConfig = TinoConfig()

variableValues = get_script_variable_values()
tinoConfig.update_job_variables(job_name=job, variables=variableValues)

execute_script(variableValues, buildConfig.get_job_script_array(job))
