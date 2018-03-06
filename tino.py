#!/usr/bin/env python

import argparse

from tino.gitlab_parser.exec_job import execute_job

parser = argparse.ArgumentParser()
parser.add_argument("stage", help="The stage of the job to execute")
parser.add_argument("job", help="The job to execute")
args = parser.parse_args()

execute_job(args.job)
