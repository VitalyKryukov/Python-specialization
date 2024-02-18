# Пользователь вводит строку текста. Подсчитайте сколько раз встречается
# каждая буква в строке без использования метода count и с ним. Результат сохраните в словаре,
# где ключ — символ, а значение — частота встречи символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

my_str1 = input("Введите строку: ")
my_set = set(my_str1)
my_dict1 = {}
# count = 0
# for i in my_set:
#     for j in range(len(my_str1)):
#         if my_str1[j] == i:
#             count += 1
#     my_dict1[i] = count
#     count = 0
# print(my_dict1)

# for item in my_set:
#     my_dict1.setdefault(item, my_str1.count(item))
# print(my_dict1)

for item in my_str1:
    my_dict1[item] = my_dict1.get(item, 0) + 1
print(my_dict1)
