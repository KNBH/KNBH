#!/usr/bin/env python3.6


import os
import signal
import const
import finder
import system


from dormitory import *


def print_help():
    "Print help message"
    print(const.HELP)


def print_header(color, block, floor):
    "Print header"
    colres = const.COLOR_RESET
    string = ''

    string += '\t\t['
    string += '%s%s%s -' % (color, block, colres)
    string += ' %s%s floor%s' % (color, str(floor), colres)
    string += ']'

    print(string)


def print_footer():
    "Print footer"
    print(" ---------------------------------")


def print_footer_ping():
    "Print footer with ping block"
    print(" --------------------------------- -------------")


def get_person(number, person):
    "Get person string"
    string = ''

    string += '| %s%s%s | ' % (const.COLOR_REGULAR_GREEN,
                               str(number), const.COLOR_RESET)

    rem = 30 + 13
    if person.female():
        string += '%s%s%s' % (const.COLOR_BOLD_RED,
                              person.full_name(), const.COLOR_RESET)
        rem += 13
    else:
        string += '%s' % (person.full_name())

    rem = rem - len(string)
    string += rem * " "
    string += "|"
    return string


def ping(host):
    "Ping specific host"
    response = os.system("ping -c 1 -w1 " + host + " > /dev/null 2>&1")
    return response == 0


def init():
    "init function"
    # both first and second case
    if (len(system.argv) == 1) or (len(system.argv) == 2 and (system.argv[1] == '-h' or system.argv[1] == '--help')):
        print_help()
        system.exit(0)

    elif len(system.argv) > 6:
        system.error('Wrong arguments!\n', 1)

    dorm = Dormitory(system.argv)

    print_header(const.COLOR_BOLD_GREEN, dorm.block().upper(), dorm.floor())

    empty_rooms = 0
    no_rooms = True
    for number in dorm.rooms():
        names = finder.get(dorm.block(), number)
        if names is None:
            # the could be no room numbers in middle of the floor
            # skip them
            if int(str(number)[-2:]) < 20:
                continue

            if empty_rooms > 0:
                # two empty rooms, stop
                # probably there are no other rooms
                break

            # maybe just empty room
            empty_rooms = empty_rooms + 1
            continue
        else:
            # reset empty rooms counter
            if empty_rooms > 0:
                empty_rooms = 0

        no_rooms = False
        if dorm.ping():
            online = 0
            room = str(number)
            if len(room) == 3 and (dorm.block().startswith("a") or dorm.block().startswith("d")):
                room = "0" + room

            for c in ["a", "b", "c"]:
                domain = str(dorm.block()) + "-" + room + c + ".kn.vutbr.cz"
                if ping(domain) or ping("w" + domain):
                    online = online + 1

            all_online = len(names) == online
            all_offline = online == 0

            print_footer_ping()
        else:
            print_footer()

        for person in names:
            if dorm.ping():
                print(get_person(number, person), end="")
                maybe = "?" if not all_online and not all_offline else ""
                if online > 0:
                    print("   " + const.COLOR_BOLD_BLUE + "online" +
                          maybe + const.COLOR_RESET + "\t|")
                    online = online - 1
                else:
                    print("   " + const.COLOR_REGULAR_YELLOW +
                          "offline" + maybe + const.COLOR_RESET + "\t|")

            else:
                print(get_person(number, person))

    if not no_rooms:
        if dorm.ping():
            print_footer_ping()
        else:
            print_footer()


###############################################################################


if __name__ == "__main__":
    signal.signal(signal.SIGINT, system.signal_handler)
    init()

