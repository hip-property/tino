from tino.gitlab_parser.build_config import BuildConfig


def get_job_args(job):
    build_config = BuildConfig.including_local_variables()
    return build_config.get_job_variables(job_name=job)
