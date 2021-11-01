from datetime import datetime
from constants import LOG_FILE


def log_init_game(counter_game):
    try:
        if counter_game == 1:
            logger = open(LOG_FILE, 'w')
            logger.write('Новая игра.\n')
        else:
            logger = open(LOG_FILE, 'a')
        logger.write('-' * 30 + f'\nИгра № {counter_game}.\n')
    except Exception as e:
        print("Произошла ошибка: ", e)
    finally:
        logger.close()


def log_start_game(mode):
    time_start_game = datetime.now()
    try:
        logger = open(LOG_FILE, 'a')
        logger.write(f'Время и дата начала игры: {datetime.ctime(time_start_game)}\n'
                     f'Выбран соперник {mode}\nХОДЫ ИГРОКОВ:\n')
    except Exception as e:
        print("Произошла ошибка: ", e)
    finally:
        logger.close()


def log_step_user(step_num, name, step):
    try:
        logger = open(LOG_FILE, 'a')
        logger.write(f"Ход №{step_num}.Игрок {name}: {step}\n")
    except Exception as e:
        print("Произошла ошибка: ", e)
    finally:
        logger.close()


def log_win(name, step_num):
    try:
        logger = open(LOG_FILE, 'a')
        logger.write(f"Победил {name} на ходу {step_num}\n")
    except Exception as e:
        print("Произошла ошибка: ", e)
    finally:
        logger.close()


def log_draw(step_num):
    try:
        logger = open(LOG_FILE, 'a')
        logger.write(f"Ничья на ходу {step_num}\n")
    except Exception as e:
        print("Произошла ошибка: ", e)
    finally:
        logger.close()