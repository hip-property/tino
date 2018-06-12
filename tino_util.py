#!/usr/bin/env python3.6

import argparse

from tino.gitlab_parser.stage_jobs import get_stage_jobs
from tino.gitlab_parser.stages import get_stages


def format_options(options):
    return ' '.join(options)


parser = argparse.ArgumentParser()
parser.add_argument("cmd", help="stages, stage-jobs, job")
parser.add_argument("-stage", help="the stage to query")
args = parser.parse_args()

if args.cmd == "stages":
    print(format_options(get_stages()))
elif args.cmd == "stage-jobs":
    if args.stage is None:
        parser.error("stage-jobs requires -stage")

    print(format_options(get_stage_jobs(args.stage)))
