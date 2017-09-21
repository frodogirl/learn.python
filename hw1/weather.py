
WEATHERS = [
    "ясно", 
    "пасмурно", 
    "дождь", 
    "ветер", 
    "снег"
]
    

DRESS = [
    "Оденься потеплее", 
    "Накинь курточку",
    "Кофты достаточно",
    "Футболка то что надо",
    "Купальник и шлёпанцы",
]

ACCESSORY = [
    "Солнечные очки",
    "Плащ на всякий случай",
    "Обязательно зонт",
    "Накинуть ветровку",
    "Нужен шарф",
]

DRESS_TO_TEMPERATURE = {
    DRESS[0]: range(-50, 0),
    DRESS[1]: range(0, 11),
    DRESS[2]: range(11, 21),
    DRESS[3]: range(21, 30),
    DRESS[4]: range(31, 51)
}

ACCESSORY_TO_WEATHER = {
    ACCESSORY[0]: WEATHERS[0],
    ACCESSORY[1]: WEATHERS[1],
    ACCESSORY[2]: WEATHERS[2],
    ACCESSORY[3]: WEATHERS[3],
    ACCESSORY[4]: WEATHERS[4]
}

def how_to_dress(temperature, weather):
    # Вот тут должен быть код для выбора одежды и аксессуара
    # Добавила словарь зависимости одежды от диапазона температуры DRESS_TO_TEMPERATURE
    # Добавила словарь зависимости аксессуаров от погоды ACCESSORY_TO_WEATHER
    
    selected_dress = ""
    selected_accessory = ""
   
    for selected_dress, temperature_range in DRESS_TO_TEMPERATURE.items():
        if temperature in temperature_range:
            break

    for selected_accessory, selected_weather in ACCESSORY_TO_WEATHER.items():
        if weather == selected_weather:
            break

    return " и ".join([selected_dress, selected_accessory])
    
if __name__ == "__main__":

    temperature = None
    weather = None
    while not temperature:
        try:
            temperature = int(input("Олаф: Сколько градусов на улице? (от -50 до +50)\nТы: "))
        except (TypeError, ValueError):
            print("Олаф: Не понял...")
            temperature = None
            continue
        if not -50 <= temperature <= 50:
            print("Олаф: Не верю!")
            temperature = None
    
    while not weather:
        weather = input("Олаф: А какая погода? ({})\nТы:  ".format(", ".join(WEATHERS)))
        if weather not in WEATHERS:
            weather = None
        elif temperature < -5 and weather == "дождь":
            print("Олаф: Дождь при отрициальной температуре?")
            weather = None
        elif temperature > 10 and weather == "снег":
            print("Олаф: Снег когда так тепло?")
            weather = None
            
    print("Олаф: {}".format(how_to_dress(temperature, weather)))

