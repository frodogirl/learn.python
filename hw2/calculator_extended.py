"""
Задача №4
---------

Файл: `calculator_extended.py`

Итак, арифмометр работает прекрасно и Олаф очень быстро добрался до 
задачек посложнее. Тут уже не хватает простых арифметических операций, 
так что Олаф решил докрутить к своему арифометру несколько 
дополнительных шестерёнок и ручек.

Необходимо написать программу, которая будет выполнять бинарные или 
унарные операции, переданные ей одной строкой. Числа могут быть не 
только целыми, но и вещественными. Возможные действия: + - / * ^ 
(возведение в степень) ! (факториал, унарная операция).

Википедия может рассказать, как возводить в степень 
(https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%B7%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B2_%D1%81%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C) или считать факториал (https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB).


Примеры:

    Введите выражение: 2+3.5
    Ответ: 5.5

    Введите выражение: 3!
    Ответ: 6
 """
from math import factorial

def to_number(input_operand):
    try:
        return int(input_operand)
    except ValueError:
        return float(input_operand)
	
def calculate_result(string_expression):
    result = 0
    # TODO: превратить строку string_expression в составные части выражения и получить результат, записав его в result
    signs = ['+', '-', '/', '*', '^', '!']
    
    for sign in signs:
        operand_list = string_expression.split(sign)
        if len(operand_list) == 2:
            if sign == signs[0]:
                # сумма
                result = to_number(operand_list[0]) + to_number(operand_list[1])
            elif sign == signs[1]:
                # вычитание
                result = to_number(operand_list[0]) - to_number(operand_list[1])
            elif sign == signs[2]:
                # деление
                result = to_number(operand_list[0]) / to_number(operand_list[1])
            elif sign == signs[3]:
                # умножение
                result = to_number(operand_list[0]) * to_number(operand_list[1])
            elif sign == signs[4]:
                # возведение в степень
                result = to_number(operand_list[0]) ** to_number(operand_list[1])
            elif sign == signs[5]:
                # факториал
                result = factorial(to_number(operand_list[0]))
    return result


if __name__ == '__main__':
    expression = input('Введите выражение: ')
    result = calculate_result(expression)
    print('Ответ: %s' % result)
