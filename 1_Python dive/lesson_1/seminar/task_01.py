# Напишите программу, которая запрашивает год и проверяет его на високосность. Распишите все возможные проверки в цепочке elif. Откажитесь от магических чисел. Обязательно учтите год ввода Григорианского календаря. В коде должны быть один input и один print.

in_year = int(input("Введите год: "))
YEAR1 = 4
YEAR2 = 100
YEAR3 = 400
result = in_year % YEAR1 == 0 and in_year % YEAR2 != 0 or in_year % YEAR3 == 0
print('Високосный' if result else 'Невисокосный')

