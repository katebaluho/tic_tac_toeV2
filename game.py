from itertools import cycle
from constants import END_GAME
from board import get_board, board_match, print_board, draw_match_board
from steps import user_step, comp_step
from users import ask_mode, create_users

MODES_STEP = {
    "COMP": {"get_step": comp_step},
    "USER": {"get_step": user_step},
}


def game_init(counter_game, **user):
    return {
        "users": create_users(ask_mode(), **user),
        "board": get_board(3),
    }

def game_cycle(users: list[dict, ...], board: list[list]):

    for step_num, user in enumerate(cycle(users), 1):
        print_board(board)

        print(f"Ход №{step_num}.Игрок {user['name']}")
        step = MODES_STEP[user['mode']]['get_step'](user, board)

        if board_match(board):
            print(f"Победил {user['name']} на ходу {step_num}\n")
            break
        if draw_match_board(step_num, board):
            print(f"Ничья на ходу {step_num}\n")
            break


def game_end():
    while True:
        user_answer = input(f'Начать новую игру? {END_GAME}')
        if not user_answer.upper() in END_GAME:
            print("Неверный выбор.Попробуйте еще раз.")
        else:
            return False if user_answer.upper() == END_GAME[0] else True
