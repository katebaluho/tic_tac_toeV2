from datetime import datetime
from src.constants import FILE_HANDLERS
from datetime import datetime

"""
Инит : Игра, Раунд, Режим игры, Имена, Время начала игры
Сycle: Игра, Раунд, Имя, Номер хода, Ход
Итог:  Игра, Раунд, Имя, Номер хода победы/Ничья
"""


def wtite_logfile(handler, message, mode = "a"):
    file = open(FILE_HANDLERS[handler], mode, encoding="UTF-8")
    try:
        file.write(message)
    except IOError:
        print("ОШИБКА ЗАПИСИ ЛОГА")
    finally:
        file.close()


def log_init_game(session, round, mode, names):
    message = f'{session}|{round}|{mode}|{names[0]}|{names[1]}|{datetime.now().ctime()}\n'
    wtite_logfile('INIT_GAME', message)


def log_game_steps(session, round, name, step_num, step:list):
    message = f'{session}|{round}|{name}|{step_num}|{step[0]}:{step[1]}\n'
    wtite_logfile('GAME_STEP', message)


def log_end_game(session, round, name, result):
    message = f'{session}|{round}|{name}|{result}\n'
    wtite_logfile('END_GAME', message)

def get_prev_session(handler):
    try:
        file = open(FILE_HANDLERS[handler], 'r', encoding="UTF-8")
    except FileNotFoundError:
        return None

    try:
        prev_session = file.read(1)
    except Exception:
        print("Ошибка чтения файла")
        return None
    finally:
        file.close()
    return prev_session

def update_session(handler):
    if not get_prev_session(handler):
        prev_session = 0
    else:
        prev_session = get_prev_session(handler)

    file = open(FILE_HANDLERS[handler], 'w', encoding="UTF-8")
    try:
        new_session = int(prev_session) + 1
        file.write(str(new_session))
    except Exception:
        print("Ошибка обновления файла")
        return None
    finally:
        file.close()
    return new_session