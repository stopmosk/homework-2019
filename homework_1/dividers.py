# Функция, возвращающая список с делителями числа
def get_dividers(num):
    num = abs(num)
    div_list = []
    for div in range(- num, num + 1):
        if div != 0:
            if num % div == 0:
                div_list.append(div)    # Заполняем список делителей
    return div_list


print(*(get_dividers(int(input('Введите число: ')))))

