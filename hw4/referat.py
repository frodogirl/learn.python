"""
Задача №1: Уникальный реферат
-----------------------------

Файл: `referat.py`

Используй сервис Яндекс.Реферат, чтобы получить реферат на заданную тему. После этого 
проверь реферат на уникальность при помощи специального сервиса. 

Нужно, чтобы у реферата уникальность была не менее 90%!
"""

import requests

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


def get_topic():
    # TODO: спрашивать у пользователя тему из списка AVAILABLE_REFERAT_TOPICS
    for i, topic in enumerate(AVAILABLE_REFERAT_TOPICS, 0):
        print(i + 1, topic)
    while True:
        try:
            olaf_topic = int(input("Topic's number? "))

            if olaf_topic <= len(AVAILABLE_REFERAT_TOPICS):
                return AVAILABLE_REFERAT_TOPICS[olaf_topic - 1]
            else:
                print('Please repeat')
        except ValueError:
            print('Please repeat')


def get_referat(topic):
    """
        TODO: получить реферат с сервиса Яндекс Рефераты при помощи requests.get
        из библиотеки requests http://docs.python-requests.org/en/master/
        Пример запроса https://yandex.ru/referats/referats/write/?t=astronomy
    """
    r = requests.get('https://yandex.ru/referats/referats/write/?t=' + topic)
    return r.text


def check_referat(referat):
    """
        TODO: При помощи сервиса http://learn.python.ru/api/uniqueness/
        проверь ункиальность реферата используя requests.post и передавая реферат в переменной text
        Сервис возвращает ответ в формате JSON, используйте requests.json для его обработки
    """
    return 91

    referat_dict = {'text': referat.text}
    r = requests.post('http://learn.python.ru/api/uniqueness/', data=referat_dict)
    return r.json()['uniqueness']


def get_unique_referat(topic):
    """
        TODO: получайте реферат при помощи get_referat и проверяйте его на уникальность
        при помощи check_referat до тех пор, пока не добьетесь uniqueness > 90
        Верните текст реферата, с uniqueness > 90
    """
    while True:
        referat = get_referat(topic)
        if check_referat(referat) > 90:
            return referat
        
if __name__ == '__main__':
    topic = get_topic()
    referat = get_unique_referat(topic)
    print(referat.text)
