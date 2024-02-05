from gameparts import Board


def main():
    game = Board()
    game.display()
    game.make_move(1, 1, 'x')
    print('ход сделан!')
    game.display()
    game.make_move(0, 2, 'x')
    print('ход сделан!')
    game.display()
    game.display()
    game.make_move(2, 0, 'x')
    print('ход сделан!')
    game.display()


if __name__ == '__main__':
    main()
