# Задание №3
# 📌 Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest

from task_01 import symbol_deleter


class TestSymbolDeleter(unittest.TestCase):

    def test_no_change(self):
        self.assertEqual(symbol_deleter('something string'), 'something string')

    def test_change_title(self):
        self.assertEqual(symbol_deleter('SOMETHING STRING'), 'something string')

    def test_punctuation(self):
        self.assertEqual(symbol_deleter('somet////hing! st....ring?'), 'something string')

    def test_foreign_letters(self):
        self.assertEqual(symbol_deleter('SOMETHINGСАМФИНГ string'), 'something string')

    def test_all(self):
        self.assertEqual(symbol_deleter('SOMETHING,,...САМФИНГ!!! string?'), 'something string')


if __name__ == '__main__':
    unittest.main(verbosity=2)
