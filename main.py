#!/usr/bin/env python3.6


import signal
import const
import finder
import system

from row import Row
from table import Table
from dormitory import Dormitory


def print_help():
    "Print help message"
    print(const.HELP)


def init():
    "init function"

    if (len(system.argv) == 1) or (len(system.argv) == 2 and (
            system.argv[1] == '-h' or system.argv[1] == '--help')):
        print_help()
        system.exit(0)

    elif len(system.argv) > 6:
        system.error('Wrong arguments!\n', 1)

    dorm = Dormitory(system.argv)

    name = "{} - {} floor".format(dorm.block().upper(), str(dorm.floor()))
    table = Table(name)

    for number in dorm.rooms():
        names = finder.get(dorm.block(), number)
        if dorm.empty_rooms():
            if names is None:
                table.add_row(Row(number)) # empty room
            else:
                continue
        elif names is not None:
            for person in names:
                table.add_row(Row(number, person))

    print(table)


###############################################################################


if __name__ == "__main__":
    signal.signal(signal.SIGINT, system.signal_handler)
    init()
