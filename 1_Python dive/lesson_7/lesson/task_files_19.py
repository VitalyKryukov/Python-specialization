text = ['1. Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        '2. Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        '3. Lorem ipsum dolor sit amet, consectetur adipisicing elit.', ]
with open('some_dir/dir/new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))
