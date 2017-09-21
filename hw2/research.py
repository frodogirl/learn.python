"""
Задача №1
---------

Файл: `research.py`

Поработав над книгой, Олаф решил, что пора бы ему всерьез заняться 
образованием. Но в его деревне нет ни одного вуза, поэтому он планирует
перебраться в город. Для начала он решил выбрать в каком районе снять
квартиру.

В файле `data/technical_education_moscow.json` содержится данные о учебных 
заведениях Москвы научно-технического направления 
(данные взяты с http://data.mos.ru/).
Для каждого заведения известны несколько параметров, в том числе 
район города, в котором это заведение находится.
Нужно вывести пятёрку районов, в которых больше всего учебных заведений.
"""

import json
import os
from collections import Counter

def load_data(path_to_file):
    with open(path_to_file, 'r') as f:
        return json.load(f)


def get_top_regions(data, top_size=5):
    # TODO: тут должен быть код, который по данным возвращает словарь вида {'название региона': количество заведений в нём}
    all_regions = [data[i]['Cells']['rayon'] for i in range(len(data))]
    count_regions = Counter(all_regions)
    return dict(count_regions.most_common()[0:5])


if __name__ == '__main__':
    data = load_data(os.path.join('data', 'technical_education_moscow.json'))
    top_regions = get_top_regions(data)
    for region, universities_amount in top_regions.items():
        print('%s: %s' % (region, universities_amount))
