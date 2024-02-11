import os
from pathlib import Path

'''Удаляем директории с несколькими уровнями вложенности
'''
# os.rmdir('dir')  # OSError
# Path('some_dir').rmdir()  # OSError
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()
