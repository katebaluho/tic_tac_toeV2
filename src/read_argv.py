import sys

MODES = {
    'COMP',
    'USER'
}

HELP_STRING = ["HELP", "help", "h", "-h"]

TERMINAL_PARAMS = {
    "mode" : '',
    "names": ['','']
}

def help():
    print("help")
    exit(0)


def read_terminal():
    try:
        param = sys.argv[1]
        if param in MODES:
            TERMINAL_PARAMS['mode'] = param
        elif param in HELP_STRING:
            help()
        else:
            raise IndexError
    except IndexError:
        pass

    if not TERMINAL_PARAMS['mode']: return None

    try:
        TERMINAL_PARAMS['names']  = sys.argv[2:]
        if not TERMINAL_PARAMS['names']  and (len(TERMINAL_PARAMS['names'] ) == 1 and TERMINAL_PARAMS['mode'].upper() == "USER"):
            return None
    except IndexError:
        pass