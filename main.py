from src.board import init_board
from src.game import game_init, game_cycle, game_end


def main():
    print("Добро пожаловать в Игру Крестики Нолики")
    game_vars = game_init()
    game_board =  init_board(3)
    while True:
        game_cycle(game_board, **game_vars)
        if game_end():
            break
        game_board =  init_board(3)
        game_vars["round"] += 1


main()