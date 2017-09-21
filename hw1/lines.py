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
