#!/usr/bin/env python
from config.format import format_options
from config.build_config import BuildConfig

try:
    config = BuildConfig()
    print(format_options(config.get_stages()))
except:
    exit()
