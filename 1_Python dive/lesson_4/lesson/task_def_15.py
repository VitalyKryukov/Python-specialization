def kwd_only_arg(*, arg):
    '''Пример только ключевой функции'''
    print(arg)


# kwd_arg(42)  # TypeError
kwd_only_arg(arg=42)

