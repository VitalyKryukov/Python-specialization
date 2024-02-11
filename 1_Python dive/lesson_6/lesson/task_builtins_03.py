import random as rnd

print(f'{rnd.random() = }')
rnd.seed(42)  # Задали отпраавную точку
state = rnd.getstate()
print(f'{state = }')
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')
rnd.setstate(state)  # Обновили статус, т.е. оптять 42
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')
