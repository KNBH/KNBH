"project constants"


MALE   = False
FEMALE = True


###############################################################################


HELP = '\nOptions:\n\n' + \
       '\tFloor:\n' + \
       '\t--floor=NUMBER\n' + \
       '\t-f=NUMBER\n\n' + \
       '\tBlock:\n' + \
       '\t--block=ID\n' \
       '\t-b=ID\n\n' + \
       '\tPing room:\n' + \
       '\t--ping\n' + \
       '\t-p\n\n' + \
       '\tRoom:\n' + \
       '\t--room\n' + \
       '\t-r\n\n'


###############################################################################

# TODO
BLOCK_MAX = 80 # max count of rooms


###############################################################################


ROW_WIDTH = 40 # length of table row


###############################################################################


COLOR_RESET = "\033[0m"

COLOR_BOLD_RED     = "\033[1m\033[31m"
COLOR_BOLD_GREEN   = "\033[1m\033[32m"
COLOR_BOLD_BLUE    = "\033[1m\033[34m"
COLOR_BOLD_YELLOW  = "\033[1m\033[33m"

COLOR_REGULAR_RED     = "\033[31m"
COLOR_REGULAR_GREEN   = "\033[32m"
COLOR_REGULAR_BLUE    = "\033[34m"
COLOR_REGULAR_YELLOW  = "\033[33m"
