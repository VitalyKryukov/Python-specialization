x = 42
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
# Получим ошибку т.к. my_list - изменяемый
# print(hash(my_list))
