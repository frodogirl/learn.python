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
