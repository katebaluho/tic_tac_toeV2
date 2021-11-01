from game import game_init, game_cycle, game_end

def main():
    print("Добро пожаловать в Игру Крестики Нолики")
    game_vars = game_init()
    while True:
        game_cycle(**game_vars)
        if game_end():
            break
        game_vars = game_init( user = game_vars['users'][0])

main()