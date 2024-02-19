# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно
# в один из вариантов ниже:
# Целое положительное число;
# Вещественное положительное или отрицательное число;
# Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква;
# Строку в нижнем регистре в остальных случаях

user = input('Введите данные:')
if user.isdigit():
    print('Integer')
elif user.count(".") == 1 and user.replace(".", "").replace("-", "").isdigit():
    print("Float")
elif any([sym.isupper() for sym in user]):
    print("Upper")
else:
    print("Lower")