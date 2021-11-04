from src.constants import FILE_HANDLERS, DELIMETER

def logging_in_file(func):
    def wrapper(handler, *args):
        message = func(handler, *args)
        try:
            with open(FILE_HANDLERS[handler], mode = 'a', encoding="UTF-8") as file:
                file.write(message)
        except IOError:
            print("ОШИБКА ЗАПИСИ ЛОГА")
        return message
    return wrapper

@logging_in_file
def log_message(handler, *args):
    message = DELIMETER.join(map(str, args))+'\n'
    return message


def get_prev_session(handler):
    try:
        with open(FILE_HANDLERS[handler], 'r', encoding="UTF-8") as file:
            prev_session = file.read(1)
    except FileNotFoundError:
        return None
    except Exception:
        print("Ошибка чтения файла")
        return None
    return prev_session

def update_session(handler):
    if not get_prev_session(handler):
        prev_session = 0
    else:
        prev_session = get_prev_session(handler)

    try:
        with open(FILE_HANDLERS[handler], 'w', encoding="UTF-8") as file:
            new_session = int(prev_session) + 1
            file.write(str(new_session))
    except Exception:
        print("Ошибка обновления файла")
        return None
    return new_session