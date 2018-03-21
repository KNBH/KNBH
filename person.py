"person module"


import const


class Person():

    def __init__(self, name, surname, gender):
        self.__name    = name
        self.__surname = surname
        self.__gender  = gender

    def name(self):
        return self.__name

    def surname(self):
        return self.__surname

    def full_name(self):
        return self.__name + " " + self.__surname

    def gender(self):
        return self.__gender

    def isFemale(self):
        return self.__gender is const.FEMALE

    def isMale(self):
        return self.__gender is const.MALE
