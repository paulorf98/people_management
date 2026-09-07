from enum import Enum, auto


class EditResult(Enum):
    ID_NOT_FOUND = auto()
    INCORRECT_PASSWORD = auto()
    EDITED = auto()