def get_dividers(num):
    # Функция, возвращающая список с делителями числа
    num = abs(num)
    div_list = []
    for div in range(-num, num + 1):
        if div:
            if not num % div:
                div_list.append(div)   # Заполняем список делителей
    return div_list


def is_prime(num):
    # Функция, определяющая, простое ли число
    if num < 2:
        return False
    div_list = get_dividers2(num)
    return len(div_list) == 4


def get_dividers2(num):
    # Версия через использование генераторов
    n = abs(num)
    return [k for k in range(-n, n + 1) if k and not n % k]


def is_prime2(num):
    # Функция, определяющая, простое ли число, v2
    return len(get_dividers2(num)) == 4 if num >= 2 else False


n = int(input('Введите число: '))
print(is_prime(n))
print(is_prime2(n))
