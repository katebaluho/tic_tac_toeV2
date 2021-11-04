import random

from src.constants import USER_TEMPLATE, COMP_NAMES, SYMBOLS
from src.read_argv import TERMINAL_PARAMS


def create_user(symbol, name) -> dict:
    user = {}
    for idx, itm in enumerate(USER_TEMPLATE):
        if name and idx == 0:
            user[itm[0]] = name if name else itm[1]
        else:
            user[itm[0]] = itm[1](symbol=symbol, mode = "USER")
    return user


def create_comp(symbol, name) -> dict:
    return {
        "name": random.choice(COMP_NAMES),
        "symbol": symbol,
        "steps": [],
        "mode": "COMP"
    }


MODES = {
    "COMP": {"creator": create_comp},
    "USER": {"creator": create_user},
}


def get_user(mode, symbol, name) -> dict:
    return MODES[mode]["creator"](symbol=symbol, name = name)


def ask_mode() -> str:
    user_modes = {idx: itm for idx, itm in enumerate(MODES, 1)}

    modes_str = "\n".join(f"{key}: {value}" for key, value in user_modes.items())
    modes_string = f"Выберите номер режима игры\n{modes_str}\n>>>"

    while True:
        try:
            mode_input = int(input(modes_string))
            return user_modes[mode_input]
        except ValueError:
            print("Недопустимый ввод, введите только число")
        except KeyError:
            print("Недопустимое значение, повторите ввод")
        continue


def create_users(mode) -> list[dict]:
    users = []
    names = TERMINAL_PARAMS['names']
    if len(names) == 1:
        names.append('')

    for symbol, mode, name in zip(SYMBOLS, ("USER", mode), names):
        user = get_user(mode, symbol, name)
        users.append(user)
    return users
