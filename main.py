from game import game_init, game_cycle, game_end

def main():
    print("Добро пожаловать в Игру Крестики Нолики")
    counter_game = 1
    game_vars = game_init(counter_game)
    while counter_game:
        game_cycle(**game_vars)
        if game_end():
            break
        counter_game += 1
        game_vars = game_init(counter_game, user = game_vars['users'][0])

main()