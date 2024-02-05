from inspect import getsource, isfunction, ismethod
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
    print(type(game))
    print(isinstance(game, Board))
    print(isinstance(game, str))
    print(dir(game))  # возвращает ВСЕ атрибуты и методы: ++ унаследованные
    print('__str__' in dir(game))
    print(hasattr(game, '__str__'))
    print(game)
    print(game.__class__.__dict__)  # возвращает атри и мет только класса
    print(getsource(Board))
    print(isfunction(game.display))
    print(ismethod(game.display))
    print(Board.__doc__)


if __name__ == '__main__':
    main()
