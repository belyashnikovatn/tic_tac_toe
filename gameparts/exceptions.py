class FieldIndexError(IndexError):
    """Обрабатывает исключения выхода за поле"""

    def __str__(self) -> str:
        return 'Введено значние за границами игрового поля'


class CellOccupiedError(Exception):
    """Обрабатывает исключение зантой ячейки"""

    def __str__(self) -> str:
        return 'Попытка изменить занятую ячейку'
