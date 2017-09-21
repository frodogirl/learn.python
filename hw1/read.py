
def calculate_read_time(text, speed):
    # Тут должен быть код, который рассчитывае время, которое 
    # понадобится чтобы прочитать текст
    return len(text.split()) * speed
    
if __name__ == "__main__":
    
    speed = None
    
    while not speed:
        try:
            speed = int(input("Олаф: Сколько слов в минуту я могу читать? (100, 500)\nТы: "))
        except (TypeError, ValueError):
            print("Олаф: Не понял...")
            speed = None
            continue
        if not 100 <= speed <= 500:
            print("Олаф: Сложно читать с такой скоростью")
            speed = None
    
    with open("book.txt", "r") as f:
        text = f.read()
    
    print(calculate_read_time(text, speed))
