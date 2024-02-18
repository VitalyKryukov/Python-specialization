import inspect

import task_01

functions_list = inspect.getmembers(task_01)

with open('__init__.py', 'a', encoding='utf-8') as f:
    for func, attribute in functions_list:
        if inspect.isfunction(attribute):
            f.write(func + '\n')
