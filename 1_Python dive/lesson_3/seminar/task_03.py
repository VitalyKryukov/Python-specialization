# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.

text = {12, "my", "our", (1, 3, "d"), True, False, 45.3, None, -87, [1, 2, 3]}
new_dict = []
for item in text:
    t = type(item)
    if t in new_dict:
        new_dict[t].append(item)
    else:
        new_dict[t] = [item]
print(new_dict)
