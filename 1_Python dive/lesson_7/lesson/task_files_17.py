text = ['1. Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        '2. Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        '3. Lorem ipsum dolor sit amet, consectetur adipisicing elit.',]
with open('some_dir/dir/new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write((line))
        print(f'{res = }\n{len(text)=}')
