"""
Задача №3
---------

Файл: `calculator.py`

Дааа, математика это не просто. Конечно, Олаф старается, но он решил 
подстарховаться и собрать себе небольшой арифмометр, чтобы быстрее 
решать задачки из учебника.

Необходимо написать программу, которая будет спрашивать у пользователя 
два целых числа и действие между ними и выполнять операцию. Например:

    Введите первое число: 8
    Введите действие: +
    Введите второе число: 22
    Ответ: 30

Возможные действия: `+ - / *`
"""

def input_expression():
    operator, operand_left, operand_right = '', 0, 0
    # TODO: предложить пользователю ввести выражение с клавиатуры и записать их в переменные operator, operand_left, operand_right
    signs = ['+', '-', '/', '*']

    while True:
        try:
            operand_left = int(input('Введите первое целое число: '))
            break
        except ValueError:
            continue
        
    while operator not in signs:
        operator = input('Введите действие (+ - / *): ')
    
    while True:
        try:
            operand_right = int(input('Введите второе целое число: '))
            break
        except ValueError:
            continue

    return {
        'operator': operator,
        'operand_left': operand_left,
        'operand_right': operand_right,
    }


def calculate_result(expression_info):
    result = 0
    # TODO: посчитать результат выражения и записать его в result
    operator = expression_info.get('operator')
    operand_left = expression_info.get('operand_left')
    operand_right = expression_info.get('operand_right')
    
    if operator == '+':
        result = operand_left + operand_right
    elif operator == '-':
        result = operand_left - operand_right
    elif operator == '/':
        result = operand_left / operand_right
    elif operator == '*':
        result = operand_left * operand_right

    return result


if __name__ == '__main__':
    expression_info = input_expression()
    expression_result = calculate_result(expression_info)
    print('Ответ: %s' % expression_result)
