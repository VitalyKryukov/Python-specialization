"""map(function, iterable)"""
text = ["Привет", "ЗДОРОВА", "привеЕствую"]
res = map(lambda x: x.lower(), text)
print(*res)  # * позволяет распаковать объект
