name = 'Alex'
age = None

a = 42
print(id(a))
a = 'Heloo world'
print(id(a))
a = 3.14 / 3
print(id(a))

print(name, age, a, 455, 'text')
print(name, age, a, 455, 'text', sep=' (=<.>=) ')
print(name, age, a, 455, 'text', sep=' (=<.>=) ', end='#')
print('Text')
print(name, age, a, 455, 'text', sep=' (=<.>=) ', end='\n')
print('Text')

res = input('Print yuor text: ')
print('Ты написал ', res)

ADULT = 18
age = int(input('Сколько тебе лет? '))
how_old = ADULT - age
print(how_old, 'Осталось до 18')




