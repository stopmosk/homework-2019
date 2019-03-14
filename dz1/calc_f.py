def calc(x, op, y):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        if y == 0:
            raise ValueError('Делить на ноль нельзя, мудила')
        else:
            return x / y
    raise Exception('Неизвестная операция')


# print(calc(1, '/', 9))
# print(calc(1, '/', 0))
# print(calc(10, '^', 10))
