"table row"


from src import const


class Row():


    def __init__(self, number, person=None):
        self.__number = number
        self.__person = person
        self.__number_length = len(str(number))
        self.__name_length = 0 if person is None else len(person.full_name())


    def number(self):
        return self.__number


    def number_length(self):
        return self.__number_length


    def name_length(self):
        return self.__name_length


    def number_colored(self):
        return "{}{}{}".format(const.COLOR_REGULAR_GREEN, str(self.__number), const.COLOR_RESET)


    def name_colored(self):
        if self.__person is None:
            return ""
        else:
            if self.__person.female():
                return "{}{}{}".format(const.COLOR_BOLD_RED, self.__person.full_name(), const.COLOR_RESET)
            else:
                return "{}".format(self.__person.full_name())
