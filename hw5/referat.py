import requests
import html5lib
import random

AVAILABLE_REFERAT_TOPICS = [
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


def get_referat(topic):
    """
        TODO: получить реферат с сервиса Яндекс Рефераты при помощи requests.get
        из библиотеки requests http://docs.python-requests.org/en/master/
        Пример запроса https://yandex.ru/referats/referats/write/?t=astronomy
    """
    html = requests.get('https://yandex.ru/referats/referats/write/?t=' + topic)
    return parse_referat(html.text)

def parse_referat(html):
    """
        TODO: При помощи библиотеки html5lib https://html5lib.readthedocs.io/en/latest/
        разобрать текст реферата на блоки и положить в словарь
        return {"div": "Текст из тега div", "strong": "Текст из тега strong", "p": ["Текст из тега p", "Текст из следующего тега p"]}
    """
    tags = {}

    document = html5lib.parse(html)
    for elem in document[1]:
    
        tag_name = elem.tag.split('}')[1]
        tag_text = elem.text
        
        if tag_name in tags.keys():
            t = tags.get(tag_name)
            
            if not(isinstance(t, list)):
                t = [t, elem.text]
            else: 
                t.append(elem.text)
            
            tag_text = t
       
        tags[tag_name] = tag_text

    return tags




if __name__ == '__main__':
    topic = 'estetica'

    referat = get_referat(topic)
    print(referat)
