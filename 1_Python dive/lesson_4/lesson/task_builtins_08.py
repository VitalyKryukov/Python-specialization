"""any(iterable)"""


def any_(iterable):
    for element in iterable:
        if not element:
            return True
    return False


numbers = [42, -73, 1024]
if any(map(lambda x: x > 0, numbers)):
    print("Хотябы один элемент положительный")
else:
    print('Все элементы не больше нуля')
