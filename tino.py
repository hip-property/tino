#!/usr/bin/env python3.6

import argparse

from tino.common.handle_interupt import handle_interrupt
from tino.gitlab_parser.exec_job import execute_job

handle_interrupt()

parser = argparse.ArgumentParser()
parser.add_argument("stage", help="The stage of the job to execute")
parser.add_argument("job", help="The job to execute")
parser.add_argument("--promptAll", help="whether to prompt for all variables", action="store_true")
args = parser.parse_args()

execute_job(args.job, args.promptAll)
