# Основная функция, возвращающая производную многочлена
def derivative_poly_s(string):
    return poly_to_str(derivative(str_to_poly(string)))


# Функция, отображающая список, содержащий полином, в строку
def poly_to_str(poly):
    poly_s = ''

    for addend in poly:
        factor, power = addend[1], addend[0]
        if factor == 0:
            continue
        # Далее, если множитель члена не равен нулю
        if factor > 0:
            poly_s += '+'
        if power == 0:
            poly_s += str(factor)
        if power == 1:
            poly_s += str(factor) + 'x'
        if power > 1:
            poly_s += str(factor) + 'x^' + str(power)

    if poly_s == '':
        poly_s = '0'
    if poly_s[0] == '+':
        poly_s = poly_s[1:]

    # print('Будем переводить полином в строку: ', end='')
    # print(poly)
    # print('Получили строку: ' + poly_s)
    return poly_s


# Функция, считающая производную многочлена (списка)
def derivative(poly):
    poly_result = []
    for poly_part in poly:
        power = poly_part[0]
        factor = poly_part[1]
        if power != 0:
            poly_result.append([power - 1, factor * power])
    # print('Посчитали производную от: ', end='')
    # print(poly)
    # print('Получили: ', end='')
    # print(poly_result)
    return poly_result


# Функция, конвертирующая строку-многочлен в список
def str_to_poly(string):
    if string == '':
        raise ValueError('Передана пустая строка')

    poly_result = []
    if string.lstrip()[0].isdigit():
        poly_s = '+' + string.replace(' ', '').rstrip('+') + '+'
    else:
        poly_s = string.replace(' ', '').rstrip('+') + '+'
    # Получили многочлен со знаком '+' или '-' слева и '+' справа

    # Заполняем список членов полинома [степень, множитель]
    buffer = ''
    for symbol in poly_s:
        if (symbol == '+' or symbol == '-') and buffer != '':
            addend = str_to_part(buffer)
            # Теперь поищем, не было ли уже подобного члена в полиноме
            # Если был - приведём подобные. Если не было - добавим как новый
            is_similar = False
            for i, poly_part in enumerate(poly_result):
                if poly_part[0] == addend[0]:
                    poly_result[i] = [poly_part[0], poly_part[1] + addend[1]]
                    is_similar = True
                    break
            if not is_similar:
                poly_result.append(addend)
            buffer = ''
        buffer += symbol

    poly_result.sort(reverse=True)
    # print('Сконвертировали строку: ' + string + ' в список:')
    # print(poly_result)
    return poly_result


# Функция, упрощающая многочлен (приведение подобных членов)
def poly_simplify(poly):
    tmp = 1
    poly_result = []
    if len(poly) == 1:
        return poly
    i = 0
    while i < len(poly) - 1:
        if poly[i][0] == poly[i + 1][0]:
            poly_result.append([poly[i][0], poly[i][1] + poly[i + 1][1]])
            i += 2
            tmp = 1
        else:
            poly_result.append([poly[i][0], poly[i][1]])
            i += 1
            tmp = 0
    if tmp == 1:
        poly_result.append([poly[i][0], poly[i][1]])
    return poly_result


# Функция, разбирающая отдельное слагаемое. Возвращает список [power, factor]
def str_to_part(string):
    pos = string.find('x')
    if pos == -1:
        factor = string
        power = '0'
    else:
        factor = string[0: pos]
        if factor == '-':
            factor = '-1'
        if factor == '' or factor == '+':
            factor = '1'
        pos = string.find('x^')
        power = '1' if pos == -1 else string[pos + 2:]
    return [str_to_int(power), str_to_int(factor)]


# Функция, преобразующая строку в число
def str_to_int(string):
    sign, current_number, digit_cnt = 1, 0, 0
    for symbol in string:
        if symbol not in set(list('+-1234567890')):
            raise ValueError('Недопустимые символы в строке.')
        if symbol == '+':
            sign = 1
        if symbol == '-':
            sign = -1
        if symbol.isdigit():
            digit_cnt += 1
            current_number = current_number * 10 + int(symbol)
            continue
    if digit_cnt == 0:
        raise ValueError('Не найдено ни одной цифры в строке')
    return sign * current_number
