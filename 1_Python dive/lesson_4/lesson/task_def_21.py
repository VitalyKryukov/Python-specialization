'''Глобальные переменные'''


def func(y: int) -> int:
    global x  # Вводим глобальную переменную
    x += 100
    print(f'In func {x = }')
    return y + 1


x = 42
print(f'In func {x = }')
z = func(x)
print(f'{x=}\t{z = }')
