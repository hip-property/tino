from tino.gitlab_parser.build_config import BuildConfig


def get_stages():
    config = BuildConfig()
    return config.get_stages()
