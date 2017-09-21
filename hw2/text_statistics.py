"""
адача №5
---------

Файл: `text_statistics.py`

Хей-хей. Оказывается, Олафом не один в этой телеге, кто едет в город, 
чтобы поступить в вуз. Вместе с ним едет Хельга, но она готовится к 
экзаменам немного иначе. У нее оказывается есть свитки, в которых 
записаны все вопросы, которые задавали на экзаменах за последние годы.
Вместе с Олафом они решают найти, каких из них задают чаще всего.


Необходимо считать текст из текстового файла `data/text.txt`, удалить 
из него знаки препинания и посчитать, какие слова как часто повторяются. 
Вывести десять самых частых слов и количество их повторений в тексте.
О том, как считать текст из файла можно прочитать, например, на 
pythonforbeginners (http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python) 
или в официальной документаци Питона (https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).
"""

import os
from collections import Counter

def load_data(path_to_file):
    # TODO: считать текст из файла path_to_file и вернуть из функции
    with open(path_to_file) as f:
         return " ".join(f.readlines()) 


def get_text_statistics(text):
    # TODO: тут должен быть код, который из текста получает и возвращает словарь вида {'слово': количество повторений слова в тексте}
    # и содержит десять самых частых слов

    signs = ['.', ',', '!', '?', ':', ';', '-', '\'', '\"', '(', ')']
    for sign in signs: 
    	text.replace(sign, '')

    words = text.split()
    #words.sort()
    count_words = Counter(words)
    return dict(count_words.most_common()[0:10])
 

if __name__ == '__main__':
    data = load_data(os.path.join('data', 'text.txt'))  # TODO: тут должен быть путь до файла с текстом (лучше положить его в папку data
    top_words = get_text_statistics(data)
    for word, repetitions in top_words.items():
        print('%s: %s' % (word, repetitions))
