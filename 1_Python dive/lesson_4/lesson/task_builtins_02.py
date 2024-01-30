"""filter(function, iterable)"""
numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))  # tuple, вместо *. т.е. на выходе получим кортеж
print(res)
