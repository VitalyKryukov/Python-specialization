def combined_example(pos_only, /, standadt, *, kwd_only):
    '''Пример функции со всеми вариантами параметров'''
    print(pos_only, standadt, kwd_only)


# combined_example(1, 2, 3)  # TypeError
combined_example(1, 2, kwd_only=3)
combined_example(1, standadt=2, kwd_only=3)
combined_example(pos_only=1, standadt=2, kwd_only=3)  # TypeError
