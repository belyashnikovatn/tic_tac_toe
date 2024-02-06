from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:
        print(f'Ход делает {current_player} игрок')

        # Запускаем бесконечный цикл для ввода коор-т
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if not 0 <= row < game.field_size:
                    raise FieldIndexError
                col = int(input('Введите номер столбца: '))
                if not 0 <= col < game.field_size:
                    raise FieldIndexError
                if game.board[row][col] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}'
                )
                print('Введите значения для сторки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячйка занята')
                print('Введите другие координаты')
                continue
            except ValueError:
                print(
                    'Буквы вводить нельзя. Только числа.',
                    'Введите значения для строки и столбца заново.'
                )
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, col, current_player)
        game.display()
        if game.check_win(current_player):
            print(f'Победил игрок {current_player}')
            running = False
        elif game.is_board_full():
            print('Ничья!')
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
