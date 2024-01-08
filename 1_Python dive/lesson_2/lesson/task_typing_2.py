def my_func(data: list[int, float]) -> float:
    res = sum(data) / len(data)
    return res


print(my_func([5, 5, 5, 5, 5]))
