#!/usr/bin/env python
import sys

from config.format import format_options
from config.build_config import BuildConfig

if len(sys.argv) != 2:
    exit()

try:
    stage = sys.argv[1]
    config = BuildConfig()

    jobsForStage = config.get_jobs_for_stage(stage)

    print(format_options(jobsForStage))
except Exception as e:
    exit()
