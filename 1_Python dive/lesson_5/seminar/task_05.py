# ✔Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# ✔Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
# ✔Для вывода результата используйте «принт» без перехода на новую строку.

for k in [0, 4]:
    for i in range(2, 11):
        res = ''
        for j in range(2 + k, 6 + k):
            res += f'{j:^2} x {i:^2} = {i * j:^2}\t'
        print(res)
    print()

print('\n\n'.join(
    ['\n'.join(['\t'.join([f'{x:>2} x {y:>2} = {x * y:>3}' for x in range(2 + k, 6 + k)]) for y in range(1, 10)]) for k
     in [0, 4]]))
