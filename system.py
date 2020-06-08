"sys wrapper"


import sys


argv = sys.argv


###############################################################################


def stdout(msg):
    sys.stdout.write(msg)


def stderr(msg):
    sys.stderr.write(msg)


def exit(num):
    sys.exit(num)


def signal_handler(signal, frame):
    stdout("\n")
    exit(0)


def error(message, exitcode):
    stderr(message)
    exit(exitcode)
