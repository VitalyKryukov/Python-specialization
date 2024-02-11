from random import randint

__all__ = ['func', '_secret']

SIZE = 100
_secret = 'qwerty'
__top_secret = '1qw3e4r5t6y'


def func(a: int, b: int) -> str:
    z = f'В диапазон от {a} до {b} получили {randint(a, b)}'
    return z


result = func(1, 6)
