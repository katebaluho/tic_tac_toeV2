from itertools import cycle
from src.constants import END_GAME
from src.board import init_board, board_match, print_board, draw_match_board
from src.logger import update_session, log_message
from src.read_argv import read_terminal, TERMINAL_PARAMS
from src.steps import user_step, comp_step
from src.users import ask_mode, create_users
from datetime import datetime


MODES_STEP = {
    "COMP": {"get_step": comp_step},
    "USER": {"get_step": user_step},
}


def game_init():
    read_terminal()

    mode = TERMINAL_PARAMS["mode"]
    if not mode:
        mode = ask_mode()

    gamevars =  {
        "session": update_session("GAME_NUM"),
        "round": 1,
        "mode" : mode,
        "users": create_users(mode),
        "start_time": datetime.now().ctime()
    }
    return gamevars

def game_cycle(board: list[list], mode:str, users: list[dict, ...], round: int, session: int, start_time):
    print('session', session)
    names = [elem['name'] for elem in users]
    log_message("INIT_GAME", session, round, mode, *names, start_time)

    for step_num, user in enumerate(cycle(users), 1):
        print_board(board)

        print(f"Ход №{step_num}.Игрок {user['name']}")
        step = MODES_STEP[user['mode']]['get_step'](user, board)
        log_message("GAME_STEP",session, round, user['name'], step_num, *step)

        if board_match(board):
            print(f"Победил {user['name']} на ходу {step_num}\n")
            log_message("END_GAME",session, round, user['name'], "WIN")
            break
        if draw_match_board(step_num, board):
            print(f"Ничья на ходу {step_num}\n")
            log_message("END_GAME",session, round, user['name'], "DRAW")
            break


def game_end():
    while True:
        user_answer = input(f'Начать новую игру? {END_GAME}')
        if not user_answer.upper() in END_GAME:
            print("Неверный выбор.Попробуйте еще раз.")
        else:
            return False if user_answer.upper() == END_GAME[0] else True
