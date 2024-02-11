last = before = 0
text = ['1. Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        '2. Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        '3. Lorem ipsum dolor sit amet, consectetur adipisicing elit.', ]
with open('some_dir/dir/new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{last = }, {before = }')
    print(f'{f.seek(before,0) = }')
    f.write('\n'.join(text))
