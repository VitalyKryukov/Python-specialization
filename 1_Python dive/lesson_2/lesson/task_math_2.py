import decimal

print(0.1 + 0.2)

pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
print(pi)
num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)
# Задаем точность до 120 символов
decimal.getcontext().prec = 120
science = 2 * pi * decimal.Decimal(23.4523446) ** 2
print(science)
