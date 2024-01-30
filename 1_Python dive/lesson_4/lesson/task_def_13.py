def func(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
    pass


def standart_arg(arg):
    '''Пример обычной функции'''
    print(arg)


standart_arg(42)
standart_arg(arg=42)
