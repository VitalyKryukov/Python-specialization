#Функция нужна для того чтобы убедиться, что у нас переменная нужного типа.

data = 42
print(isinstance(data, int))

#True and False - является подкласом int
data = True
print(isinstance(data, int))

data = 3.14
print(isinstance(data, (int, float, complex)))
