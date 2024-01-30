"""iter(object[, sentinel])"""

a = 42
# iter(a)  # TypeError: 'int' is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)  # Важно, для печати
print(*list_iter)  # Проитерировать можно 1 раз
