# Таблица умножения
for k in [0, 4]:
    for i in range(2, 11):
        res = ''
        for j in range(2 + k, 6 + k):
            res += f'{j:^2} x {i:^2} = {i * j:^2}\t'
        print(res)
    print()