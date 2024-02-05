class Board:
    """Класс, который описывает игровое поле"""

    field_size = 3

    # инициализировать новое поле
    def __init__(self) -> None:
        self.board = [[' ' for _ in range(self.field_size)]
                      for _ in range(self.field_size)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self) -> str:
        return (
                'Объект игрового поля размером '
                f'{self.field_size}x{self.field_size}'
                )
