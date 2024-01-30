def mean(args):
    return sum(args) / len(args)


print(mean([1, 2, 3]))
# print(mean(1, 2, 3))  # TypeError


def mean(*args):
    return sum(args) / len(args)


print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))
