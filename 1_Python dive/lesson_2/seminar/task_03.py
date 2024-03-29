# ✔ Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

num = int(input('Введите целое число: '))


def tobase(num: int, base: int):
    result = ''
    while num > 0:
        result = str(num % base) + result
        num //= base
    return result


print(tobase(num, 2))
print(bin(num))
print(tobase(num, 8))
print(oct(num))
