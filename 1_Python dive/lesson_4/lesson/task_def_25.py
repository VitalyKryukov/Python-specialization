def max_befor_hundred(*args):
    """Return the maximum number not exceeding 100."""
    m = float('-inf')
    for item in args:
        if m < item < 100:
            m = item
    return m


print(max_befor_hundred(-42, 73, 256, 0))
