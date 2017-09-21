
def split_to_colums(text, columns, width, offset):
    # Тут нужно разбить текст на строки ограниченной длины
    return text

# Не обращай внимания на то что идет ниже

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
