from tino.gitlab_parser.build_config import BuildConfig


def get_stage_jobs(stage):
    config = BuildConfig.including_local_variables()
    return config.get_jobs_for_stage(stage)
