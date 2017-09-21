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
