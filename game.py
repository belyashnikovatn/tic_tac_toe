from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    game.display()

    # Запускаем бесконечный цикл
    while True:
        try:
            row = input('Введите номер строки: ')
            if any(map(str.isalpha, row)):
                raise ValueError
            else:
                row = int(row)
            if not 0 <= row < game.field_size:
                raise FieldIndexError
            col = input('Введите номер столбца: ')
            if any(map(str.isalpha, col)):
                raise ValueError
            else:
                col = int(col)
            if not 0 <= col < game.field_size:
                raise FieldIndexError
        except ValueError:
            print(
                'Буквы вводить нельзя. Только числа.',
                'Пожалуйста, введите значения для строки и столбца заново.'
            )
            continue
        except FieldIndexError:
            print(
                'Значение должно быть неотрицательным и меньше '
                f'{game.field_size}'
            )
            print('Пожалуйста, введите значения для сторки и столбца заново.')
            continue
        except Exception as e:
            print(f'Возникла ошибка: {e}')
            continue
        else:
            break
    game.make_move(row, col, 'x')
    print('ход сделан!')
    game.display()


if __name__ == '__main__':
    main()
