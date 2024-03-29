# Функция, печатающая строку с пробелами между буквами
def print_word(string):
    for s in string:
        print(s + ' ', end='')
    print()


# Функция для проверки введённой буквы на соответствие
def check_letter(ltr_list, letter):
    if letter == '':
        return False
    if len(letter) > 1:
        print('Введите ровно одну букву.')
        return False
    smb = letter[0]
    if not 'а' <= smb <= 'я' and not 'А' <= smb <= 'Я':
        print('Буква должна быть из диапазона а..я или А..Я')
        return False
    if letter in ltr_list:
        print('Такая буква уже была.')
        return False
    return True


# Функция, генерирующая табло по слову и уже известным буквам
def generate_string(string, exist_letters):
    result = ''
    for s in string:
        result += s if s in exist_letters else '_'
    return result
