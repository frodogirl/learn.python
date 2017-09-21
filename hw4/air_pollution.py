import requests

# Это словарь, в котором ключи - это нужные нам параметры загрязнения,
# а значения - уровень их вредности. Мы будем исользовать его для
# нескольких задач. Во-первых, проверять полученные данные на предмет
# нужны ли они нам или пропустить. Во-вторых, он нам понадобится для
# рассчета итогового коэффициента загрязнения

params = {
    'Взвешенные частицы РМ2.5': 3, 'Метан': 3, 'Бензол': 5,
    'Оксид азота': 1, 'Диоксид азота': 3, 'Аммиак': 3, 'Сероводород': 4,
    'Озон': 1, 'Диоксид серы': 1, 'Сумма углеводородных соединений': 3,
    'Фенол': 2, 'Формальдегид': 4, 'Оксид углерода': 5,
    'Взвешенные частицы РМ10': 3
}

# Это ссылка на источник, из которого мы скачаем данные о загрязнении
# воздуха. Это самые настоящие и довольно актуальные данные,
# опубликованные правительство Москвы
SOURCE_URL = "http://api.data.mos.ru/v1/datasets/2453/rows"

# Эта функция должна получить данные по указанной ссылке
# разобрать их как json и вернуть уже в виде python-объекта.
def get_json_data_from_server(url):
    r = requests.get(url, {'api_key': ''}) # добавить api_key с портала api.data.mos.ru
    print(r.status_code)
    return r.json()


# А эта функция должна, принимая в качесве аргумента данные полученные
# от источника, создать словарь, в котором ключ - название района,
# а значение - словарь загрязнений. В котором ключи - названия типов
# загрязнения, а значения - их уровень.
def make_pollution_dict(data):
    # Пустой словарь, который надо будет заполнить данными о различных
    # параметрах загрязнения в разных районах.
    pollution = {}

    # Чтобы понять структуру данных, полученных с сервиса, не стесняйся
    # использовать print, а так же методы словарей .keys() и .values()

    # В качестве уровня загрязнения нас будет интересовать значение
    # с ключом MonthlyAverage

    # WARNING! В данных, которые мы получим, типы загрязнения
    # не всегда строковые. Иногда там попадаются словари. Поэтому тебе 
    # потребуется проверять, не словарь ли это, и если словарь - 
    # доставать знаение из него. Звучит срашно, поэтому подсказка:
    # Если параметр сохранен в переменную parameter

    # if type(parameter) is dict:
    #     parameter = parameter['value']

    # И не забывай проверять - присутствует ли полученный параметр 
    # в ключах словаря params

    for cells in data:
        cell = cells.get('Cells')
        parameter = cell.get('Parameter')

        if isinstance(parameter, dict):
            parameter = parameter['value']

        if parameter in params:
            district = cell.get('District')
            monthly_average = cell.get('MonthlyAverage')
            if district in pollution.keys():
                pollution.get(district)[parameter] = monthly_average
            else:
                pollution[district] = {parameter: monthly_average}

    return pollution


# А эта функция должна рассчитать нам общие уровни загрязнения каждого
# района. Алгоритм рассчета такой:
# Сумма произведений всех загрязнений на их вес.
# ∑ (pollution_level*pollution_weight)
# Результат добавить в словарю загрязнений района, с ключом total
def calculate_pollution_level(pollution):
    for district, district_pollution in pollution.items():
        pollution_total = 0
        for pollution_name, pollution_level in district_pollution.items():
            pollution_total += pollution_level * params.get(pollution_name, 0)
        district_pollution['total'] = round(pollution_total, 4)
    return pollution

if __name__ == "__main__":
    raw_data = get_json_data_from_server(SOURCE_URL)
    pollution = make_pollution_dict(raw_data)
    leveled_pollution = calculate_pollution_level(pollution)
    for district, district_pollution in leveled_pollution.items():
        print(district, district_pollution['total'])
