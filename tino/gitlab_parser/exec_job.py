from tino.bash_utils.bash_executor import execute_script
from tino.gitlab_parser.build_config import BuildConfig
from tino.gitlab_parser.tino_config import TinoConfig


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


def get_script_variable_values(build_config, tino_config, job):
    variable_names = build_config.get_job_variables(job_name=job)
    default_values = tino_config.get_job_variables(job_name=job)
    hardcoded_values = build_config.get_variables()
    variable_values = {}
    for variable_name in sorted(set(variable_names)):
        variable_values[variable_name] = get_variable_value(variable_name, hardcoded_values, default_values)

    return variable_values


def execute_job(job, prompt_for_all_variables):

    build_config = BuildConfig.including_local_variables() \
        if prompt_for_all_variables \
        else BuildConfig.ignoring_local_variables()

    tino_config = TinoConfig()

    variable_values = get_script_variable_values(build_config, tino_config, job)
    tino_config.update_job_variables(job_name=job, variables=variable_values)

    execute_script(variable_values, build_config.get_job_script_array(job))
