
"""
Задача №3
---------

Файл: `articles.py`

Отлично, Олаф уже умеет собирать странички для печати. Но, что же ему
печатать в книге? Давайте отправим Олафа за материалом для книги на
Яндекс.Рефераты.

В файле `articles.py` есть две готовые функции которые возвращают
заголовок и текст статьи с заданной темой.

Нам надо написать код, который cгенерирует таким образом 10 статей.
Каждая статья - это словарь (dict) у которого есть два ключа: title и 
text. Эти статьи надо сложить в список (list), а потом записать на диск 
в файл `articles.json`
"""

from urllib.parse import urlencode
from urllib.request import urlopen
import json

AVAILABLE_ARTICLE_THEMES = [
    'astronomy',
    'geology',
    'gyroscope',
    'literature',
    'marketing',
    'mathematics',
    'music',
    'polit',
    'agrobiologia',
    'law',
    'psychology',
    'geography',
    'physics',
    'philosophy',
    'chemistry',
    'estetica'
]

def generate_title():
    raw_title = urlopen('https://referats.yandex.ru/creator/write/').read()
    return raw_title.decode('utf-8').capitalize()


def generate_article():
    url_template = 'https://referats.yandex.ru/referats/write/?%s'
    url = url_template % urlencode({'t': '+'.join(AVAILABLE_ARTICLE_THEMES)})
    raw_text = urlopen(url).read().decode('utf-8')
    article = '<p>%s' % '<p>'.join(raw_text.split('<p>')[1:])
    return article


if __name__ == "__main__":
    articles = [{generate_title(): generate_article()} for i in range(10)]
    
    with open("articles.json", "w", encoding='utf-8') as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)       
    