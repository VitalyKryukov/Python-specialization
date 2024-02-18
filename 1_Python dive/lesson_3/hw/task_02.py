# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами. Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.
import re
from collections import Counter

text = "Python 3.9 is the latest version of Python. It's awesome!"

words = re.sub(r'[^\w\s]','',text.replace('\'',' ').lower()).split()
word_counter = Counter()
for word in words:
        if not word.isdigit():
            word_counter[word] += 1
print(word_counter.most_common(10))

# # Удаляем знаки препинания и приводим текст к нижнему регистру
# cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# # Разбиваем текст на слова и считаем их количество
# words = cleaned_text.split()
# word_counts = {}

# for word in words:
#     if word not in word_counts:
#         word_counts[word] = 1
#     else:
#         word_counts[word] += 1

# # Получаем 10 самых часто встречающихся слов
# top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# print(top_words)
