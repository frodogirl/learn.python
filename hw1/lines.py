"""
Задача №2
---------

Файл: `lines.py`

На заре книгопечатания, задолго до принтеров, текст для оттиска страницы
собирали вручную. И тогда текст, написаный от руки, надо было разбивать 
на строки определенной ширины. Недавно Олаф откопал в кладовке срарую 
книгопечатную машинку, но не знает как подготовить текст для печати.


В файле `lines.py` есть функция `split_to_lines`, которая принимает 2 
аргумента - текст и максимальную ширину строки. Твоя задача, разбить
входящий текст на строки таким образом, чтобы ширина каждой не превышала
максимального значения. Но, самое главное состоит в том, что нельзя 
разбивать слова - переносить на новую строчку можно только по пробелам
или знакам пунктуации.

Кстати, в этот раз Олаф спросит тебя только о максимально ширине строки.
Сам текст он возьмет из файла `lines.txt`, так что если захочешь 
поэкспериментировать с текстом - можешь заменить текст в этом файле.
"""

def split_to_lines(text, width):
    # Тут нужно разбить текст на строки ограниченной длины.
    signs = [" ", "\n", ".", ",", ":", ";", "!", "?"] # знаки, по которым можно переносить      
    lines = []

    start = 0
    
    while start + width < len(text):
        shift = 0
        end_of_line = text[start + width - 1 + shift]
        
        while end_of_line not in signs:
            shift -= 1
            end_of_line = text[start + width - 1 + shift]

        lines.append(text[start: start + width + shift].strip())
        start += width + shift
        
    lines.append(text[start:].strip())        

    return "\n".join(lines)

if __name__ == "__main__":
    
    with open("lines.txt", "r") as f:
        text = f.read()
    
    width = None
    while not width:
        try:
            width = int(input("Олаф: Какой ширины строка? (40 - 120)\nТы: "))
        except (TypeError, ValueError):
            print("Олаф: Не понял...")
            width = None
            continue
        if not 40 <= width <= 80:
            print("Олаф: Нет, так я не смогу")
            width = None
            
    print(split_to_lines(text, width))
