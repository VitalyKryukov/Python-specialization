link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/')
print(urls)

a, b, c = input('Введите 3 числа через пробел: ').split()
print(a, b, c)
a, b, c, *_ = input('Введите не менее 3-х чисел через пробел: ').split()
print(a, b, c)
