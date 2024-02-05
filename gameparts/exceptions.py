class FieldIndexError(IndexError):
    """Обрабатывает исключения выхода за полел"""

    def __str__(self) -> str:
        return 'Введено значние за границами игрового поля'
