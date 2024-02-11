import os
from pathlib import Path

print(os.getcwd())
print(Path.cwd())
os.chdir('../..')  # Перешли на 2 папки выше
print(os.getcwd())
print(Path.cwd())
