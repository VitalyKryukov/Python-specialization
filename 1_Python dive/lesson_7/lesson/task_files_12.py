with open('text_data.txt', 'r', encoding='utf_8') as f:
    while res := f.readline():
        print(res)
