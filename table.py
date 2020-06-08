"output table"

import const
from itertools import groupby


class Table():
    def __init__(self, name):
        self.__table_name = name
        self.__table_name_length = len(name)
        self.__rows = list()

    def add_row(self, row):
        self.__rows.append(row)

    def __str__(self):
        rowsize = const.ROW_WIDTH
        string = ""

        ws_count = (rowsize - self.__table_name_length) / 2

        string += "{}[{}{}{}]\n".format(
            round(ws_count) * ' ',
            const.COLOR_BOLD_GREEN,
            self.__table_name, const.COLOR_RESET
        )

        string += "+" + (rowsize - 2) * '-' + "+\n"

        for key, group in groupby(self.__rows, lambda x: x.number()):
            for row in group:
                row_str = "| {} | {}".format(str(row.number_colored()), row.name_colored())

                # 6 = template_size (5) + ending_pipe (1)
                ws_count = rowsize - (row.number_length() + row.name_length() + 6)

                string += row_str + ws_count * ' ' + "|\n"
            string += "+" + (rowsize - 2) * '-' + "+\n"

        return string.rstrip()
