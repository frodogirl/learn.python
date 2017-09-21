def input_coefficients():
    a, b, c = 0, 0, 0
    # TODO: тут нужно заполнить a, b и с значениями, введёнными пользователем
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    return a, b, c


def get_square_roots(a, b, c):
    root1, root2 = 0, 0
    # TODO тут нужно решить квадратное уравнение и записать корни в переменные root1, root2
    d = b ** 2 - 4 * a * c
    if d > 0:
        root1 = (-b + d ** 0.5) / (2 * a)
        root2 = (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        root1 = root2 = -b / (2 * a)
    else:
        root1 = root2 = None     

    return root1, root2


if __name__ == '__main__':
    a, b, c = input_coefficients()
    root1, root2 = get_square_roots(a, b, c)
    print('Корни уравнения: %s, %s' % (root1, root2))
