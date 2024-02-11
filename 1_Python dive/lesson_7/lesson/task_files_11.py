SIZE = 100
with open('text_data.txt', 'r', encoding='utf_8') as f:
    while res := f.read((SIZE)):
        print(res)
