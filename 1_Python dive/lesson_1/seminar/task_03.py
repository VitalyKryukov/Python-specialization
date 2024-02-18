# Нарисовать вконсоли елку, спросив у пользователя количество рядов

SPACE = ' '
SRAR = '*'
rows = int(input('Введите количество рядов: '))
spaces = rows - 1
stars = 1
for _ in range(rows):
    print(SPACE * spaces + SRAR * stars)
    stars += 2
    spaces -= 1

