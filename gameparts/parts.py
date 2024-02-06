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

    def is_board_full(self):
        return all([self.board[row][col] != ' ' for row in
                    range(self.field_size) for col in range(self.field_size)])

    def check_win(self, player):
        for row in range(self.field_size):
             if (
                all([self.board[row][col] == player for col
                      in range(self.field_size)]) or
                all([self.board[col][row] == player for col
                      in range(self.field_size)]) or
                all([self.board[col][col] == player for col
                      in range(self.field_size)]) or
                all([self.board[col][self.field_size - col - 1] == player 
                     for col in range(self.field_size)])
                     ): return True
        return False

    def __str__(self) -> str:
        return (
                'Объект игрового поля размером '
                f'{self.field_size}x{self.field_size}'
                )
