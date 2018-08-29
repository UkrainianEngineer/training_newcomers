"""
This module calls a bash script that searches for running
python processes and displays PID's of these processes
"""

import argparse
from subprocess import call

parser = argparse.ArgumentParser()
parser.add_argument('--search', help='search for python process')
args = parser.parse_args()

argument = str(args.search)

call(['./search_python.sh', argument])

