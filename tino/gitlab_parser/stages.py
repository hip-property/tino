from tino.gitlab_parser.build_config import BuildConfig


def get_stages():
    config = BuildConfig.including_local_variables()
    return config.get_stages()
