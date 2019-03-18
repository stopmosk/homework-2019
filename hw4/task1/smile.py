from smile_logic import is_correct


s = input('Введите строку для тестирования скобок: ')
print('Отлично') if is_correct(s) else print('Плохо. Проверьте скобки')
