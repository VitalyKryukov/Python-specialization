import random as rnd

data = [2, 4, 6, 8, 42, 73]

print(f'{data} = ')
rnd.shuffle(data)  # Перемешает элементы списка
print(f'{data = }')

print(f'{rnd.sample(data,3) = }')  # Вернет три случайных элемента
""" Вернет 3 случайных числа, где
counts = [] - отвечаеет за количество элементов в списке data
т.е. 2-к теперь 1, а 73 100
"""
print(f'{rnd.sample(data, 3, counts=[1, 1, 1, 1, 1, 100]) = }')
