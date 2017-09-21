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
