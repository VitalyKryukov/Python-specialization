def pos_only_arg(arg, /):
    '''Пример только позиционной функции'''
    print(arg)


pos_only_arg(42)
pos_only_arg(arg=42)  # TypeError
