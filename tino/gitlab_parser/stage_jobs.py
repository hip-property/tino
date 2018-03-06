from tino.gitlab_parser.build_config import BuildConfig


def get_stage_jobs(stage):
    config = BuildConfig()
    return config.get_jobs_for_stage(stage)
