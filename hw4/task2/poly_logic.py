# Основная функция, возвращающая производную многочлена
def derivative_poly_s(string):
    return poly_to_str(derivative(str_to_poly(string)))


# Функция, отображающая список, содержащий полином, в строку
def poly_to_str(poly):
    poly_result = ''
    for addend in poly:
        power = addend[0]
        factor = addend[1]
        if poly_result == '':
            poly_result += (str(factor))
        else:
            poly_result += (' + ' + str(factor))
        if power == 1:
            poly_result += 'x'
        elif power > 1:
            poly_result += 'x^' + str(power)
    if poly_result == '':
        poly_result = '0'
    return poly_result


# Функция, считающая производную многочлена (списка)
def derivative(poly):
    poly_result = []
    for poly_part in range(len(poly)):
        power = poly[poly_part][0]
        factor = poly[poly_part][1]
        if power != 0:
            poly_result.append([power - 1, factor * power])
    return poly_result


# Функция, конвертирующая строку-многочлен в список
def str_to_poly(string):
    poly_result = []
    buffer = ''
    for s in string.replace(' ', ''):
        if (s == '+' or s == '-') and buffer != '':
            poly_result.append(str_to_part(buffer))
            buffer = ''
        buffer += s
    addand = str_to_part(buffer)
    flag = 0
    for poly_part in poly_result:
        if [poly_part][0] == addand[0]:
            poly_result = [poly_part[0], poly_part[1] + addand[1]]
            flag = 1
            break
    if flag == 0:
        poly_result.append(addand)
    poly_result.sort(reverse=True)
    # pack_poly(poly_result)
    return poly_result


# Функция, приводящая подобные члены полинома
def pack_poly(poly):
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
