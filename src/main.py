"the main"


import os
import signal

from src import row as r
from src import table as t
from src import dormitory as d
from src import const, finder, system


def print_help():
    "Print help message"
    print(const.HELP)


def init():
    "init function"

    signal.signal(signal.SIGINT, system.signal_handler)

    if (len(system.argv) == 1) or (len(system.argv) == 2 and (system.argv[1] == '-h' or system.argv[1] == '--help')):
        print_help()
        system.exit(0)

    elif len(system.argv) > 6:
        system.error('Wrong arguments!\n', 1)

    dorm = d.Dormitory(system.argv)

    name = "{} - {} floor".format(dorm.block().upper(), str(dorm.floor()))
    table = t.Table(name)

    for number in dorm.rooms():
        names = finder.get(dorm.block(), number)
        if names is None:
            if dorm.empty_rooms():
                table.add_row(r.Row(number)) # empty room
            else:
                continue
        else:
            for person in names:
                table.add_row(r.Row(number,person))

    print(table)
