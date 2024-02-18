class Count:
    _count = 0
    _last = None

    def __new__(cls, *args, **kwargs):
        if cls._count < 3:
            cls._last = super().__new__(cls)
            cls._count += 1
        return cls._last

    def __init__(self, name: str):
        self.name = name


a1 = Count('Первый')
print(f'{a1.name =}')
a2 = Count('Второй')
print(f'{a2.name =}')
a3 = Count('Третий')
print(f'{a3.name =}')
a4 = Count('Четвертый')
print(f'{a4.name =}')
