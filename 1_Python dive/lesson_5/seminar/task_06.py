# ✔Создайте функцию-генератор.
# ✔Функция генерирует N простых чисел, начиная с числа 2.
# ✔Для проверки числа на простоту используйте правило: «число является простым,
# если делится нацело только на единицу и на себя».

def simple_generator(limit: int):
    yield 2
    number = 3
    turn = 1
    while turn < limit:
        for dev in range(3, int(number ** 0.5) + 1, 2):
            if not number % dev:
                break
        else:
            yield number
            turn += 1
        number += 2


generator = simple_generator(10)
for prime in generator:
    print(prime, end=' ')
print()
