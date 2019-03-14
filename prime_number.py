# Функция, возвращающая список с делителями числа
def get_dividers(num):
    num = abs(num)
    div_list = []
    for div in range(- num, num + 1):
        if div != 0:
            if num % div == 0:
                div_list += [div]   # Заполняем список делителей
    return div_list

# Функция, определяющая, простое ли число
def is_prime(num):
    if num < 2:
        return False
    div_list = get_dividers(num)
    if len(div_list) == 4:
        return True
    else:
        return False


print(is_prime(int(input('Введите число: '))))
