from lesson_6.lesson.mathematical import base_math

x = base_math.mul  # Плохой пример
y = base_math._START_MULT  # Очень плохой пример, получили доступ к защищенной переменной
z = base_math.sub(73, 42)
print(x(2, 3))
print(y)
print(z)
