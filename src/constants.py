import os
from settings import LOG_FOLDER

SYMBOLS = ("X", "O")

END_GAME = ('Y', 'N')


COMP_NAMES = [
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
]


USER_TEMPLATE = (
    ("name", lambda *args, **kwargs: input("ВВЕДИТЕ ВАШЕ ИМЯ")),
    ("symbol", lambda symbol, *args, **kwargs: symbol),
    ("steps", lambda *args, **kwargs: list()),
    ("mode", lambda mode, **kwargs: mode)
)


FILE_HANDLERS = {
    "GAME_NUM": os.path.join(LOG_FOLDER, "game_num_inc"),
    "INIT_GAME": os.path.join(LOG_FOLDER, "game_init"),
    "GAME_STEP": os.path.join(LOG_FOLDER, "game_log"),
    "END_GAME": os.path.join(LOG_FOLDER, "end_game"),
}