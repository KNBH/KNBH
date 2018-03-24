"dormitory module"


import re
import system


class Dormitory():


    def __init__(self, argv):
        self.__block = None
        self.__floor = None
        self.__ping = False
        self.__room = None

        for arg in argv[1:]:

            if re.match('^--block=.+$', arg):
                self.__block = check_block(arg[8:])
            elif re.match('^-b=.+$', arg):
                self.__block = check_block(arg[3:])

            elif re.match('^--floor=.+$', arg):
                self.__floor = check_number(arg[8:])
            elif re.match('^-f=.+$', arg):
                self.__floor = check_number(arg[3:])

            elif re.match('^--room=.+$', arg):
                self.__room = check_number(arg[7:])
            elif re.match('^-r=.+$', arg):
                self.__room = check_number(arg[3:])
                self.__floor = room_to_floor(self.__room)

            elif re.match('^--ping$', arg) or re.match('^-p$', arg):
                self.__ping = True

            else:
                system.error('Wrong arguments!\n', 1)


    def block(self):
        return self.__block


    def floor(self):
        return self.__floor


    def ping(self):
        return self.__ping


    def rooms(self):
        if self.__room != None:
            return range(self.__room, self.__room + 1)
        a = self.__floor * 100
        b = (a + 100) - 1
        return range(a, b + 1)


###############################################################################


def check_block(string):
    if re.match('^(B0[2457]|A0[2-5]|C0[1-3])$', string, re.IGNORECASE):
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
