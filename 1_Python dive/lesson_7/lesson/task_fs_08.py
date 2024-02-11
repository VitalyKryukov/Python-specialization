"""Получить информацию о текущем каталоге со всем его содержимым"""
import os
from pathlib import Path

print(os.listdir())  # Список list всего что находится в текущем каталоге

p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)
