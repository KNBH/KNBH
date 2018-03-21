"dormitory module"


import re
import system
import const


class Dormitory():


    def __init__(self, argv):
        self.__block = None
        self.__floor = None
        self.__ping = False
        self.__boysOnly = False
        self.__girlsOnly = False
        self.__room = None
        self.__empty_rooms = False

        for arg in argv[1:]:

            # BLOCK
            if re.match('^--block=.+$', arg):
                self.__block = check_block(arg[8:])
            elif re.match('^-b=.+$', arg):
                self.__block = check_block(arg[3:])

            # FLOOR
            elif re.match('^--floor=.+$', arg):
                self.__floor = check_number(arg[8:])
            elif re.match('^-f=.+$', arg):
                self.__floor = check_number(arg[3:])

            # ROOM
            elif re.match('^--room=.+$', arg):
                self.__room = check_number(arg[7:])
                self.__floor = room_to_floor(self.__room)
            elif re.match('^-r=.+$', arg):
                self.__room = check_number(arg[3:])
                self.__floor = room_to_floor(self.__room)

            # ENABLE EMPTY ROOM PRINTING
            elif re.match('^--empty$', arg) or re.match('^-e$', arg):
                self.__empty_rooms = True

            elif re.match('^--ping$', arg) or re.match('^-p$', arg):
                self.__ping = True

            # ENABLE FILTERS BY GENDER
            elif re.match('^--girls$', arg) or re.match('^-G$', arg):
                self.__girlsOnly = True

            elif re.match('^--boys$', arg) or re.match('^-B$', arg):
                self.__boysOnly = True

            # UNSUPPORTED ARGS
            else:
                system.error('Wrong arguments!\n', 1)

        if self.__block.startswith(('b', 'B')):
            if self.__block.endswith(('4', '7')):
                self.__max = 22
            else:  # 5 and 2
                self.__max = 39
        elif self.__block.startswith(('a', 'A')):
            self.__max = 41
        elif self.__block.startswith(('d', 'D')):
            self.__max = 30
        elif self.__block.startswith(('c', 'C')):
            self.__max = 32


    def block(self):
        return self.__block

    def floor(self):
        return self.__floor

    def empty_rooms(self):
        return self.__empty_rooms

    def ping(self):
        return self.__ping

    def girlsOnly(self):
        return self.__girlsOnly

    def boysOnly(self):
        return self.__boysOnly

    def rooms(self):
        if self.__room != None:
            return range(self.__room, self.__room + 1)
        else:
            a = self.__floor * 100
            b = (a + self.__max + 1)
            return range(a, b)


###############################################################################


def check_block(string):
    if re.match('^(B0[2457]|A0[2-5]|C0[1-3]|D0[1-2])$', string, re.IGNORECASE):
        return string.lower()
    else:
        system.error(string+'\nWrong block!\n', 3)


def check_number(string):
    try:
        number = int(string)
    except ValueError:
        system.error(string+'\nWrong number!\n', 2)
    if number >= 0:
        return number
    else:
        system.error(string+'\nWrong number!\n', 2)


def room_to_floor(number):
    room = str(number)
    if len(room) == 3:
        return room[:1]
    else:
        return room[:2]
