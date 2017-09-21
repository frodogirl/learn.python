"""
Задача №4
---------

Файл: `pagination.py`

Итак, у нас есть материал и Олаф уже почти готов печатать свою книгу.
Собственно, осталось разбить весь накопленный материал на страницы.

В файле `pagination.py` есть функция `get_page_content`, которая принимает
3 аргумента - список статей, номер страницы и количество статей на 
странице. Вернуть эта функция должна статьи, которые попадут на 
указанную страницу.

Например, при выводе 6й страницы по 4 статьи должны быть выведены 
статьи 21-24.

Статьи, кстати, берутся из файла `100articles.json`, который создан так же,
как в прошлом уроке, просто их там 100.
"""

import json

def get_page_content(articles, page, perpage):
    
    # Тут должен быть код, который разобьет список статей на страницы
    # нужного размера, найдет указаную страницу и вернет её статьи
    
    return articles[page * perpage - perpage + 1: page * perpage + 1]

if __name__ == "__main__":
    
    page = None
    perpage = None
    
    while not perpage:
        try:
            perpage = int(input("Олаф: Сколько статей уместить на страницу? (1, 100)\nТы: "))
        except (TypeError, ValueError):
            print("Олаф: Не понял...")
            perpage = None
            continue
        if not 1 <= perpage <= 100:
            print("Олаф: У меня всего 100 статей")
            perpage = None
        
    while not page:
        try:
            page = int(input("Олаф: И какая страница? (1, 100)\nТы: "))
        except (TypeError, ValueError):
            print("Олаф: Не понял...")
            page = None
            continue
        if not 1 <= perpage <= 100:
            print("Олаф: Странный номер для страницы")
    
    with open("100articles.json", "r") as f:
       articles = json.load(f)
    
    print(get_page_content(articles, page, perpage))
