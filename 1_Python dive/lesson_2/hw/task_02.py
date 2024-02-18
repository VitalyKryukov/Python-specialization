# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"


def add_mult(frac1, frac2, operation):
    num1, denom1 = map(int, frac1.split("/"))
    num2, denom2 = map(int, frac2.split("/"))
    if operation == 's':
        tmp_num = num1 * denom2 + num2 * denom1
    else:
        tmp_num = num1 * num2
    tmp_denom = denom1 * denom2
    return f"{tmp_num}/{tmp_denom}"


print("Сумма дробей:", add_mult(frac1, frac2, 's'))
print("Произведение дробей:", add_mult(frac1, frac2, 'm'))

print("Сумма дробей:", Fraction(frac1) + Fraction(frac2))
print("Произведение дробей:", Fraction(frac1) * Fraction(frac2))
