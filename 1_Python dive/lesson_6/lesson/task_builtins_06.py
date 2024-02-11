import random
from sys import argv

print(random.uniform(int(argv[1]), int(argv[2])))
print(random.randrange(int(argv[1]), int(argv[2]), int(argv[1])))
print(random.sample(range(int(argv[1]), int(argv[2]), int(argv[1])), 10))

"""Запускаем скрипт
python .\task_builtins_06.py 10 1010  
Вывод:
356.6099639567106
480
[160, 240, 480, 670, 100, 430, 840, 40, 560, 680]
"""