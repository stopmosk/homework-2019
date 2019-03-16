from caesar_logic import encrypt, decrypt

print('Добрейший вечерочек. Будем щифровать (e) или расщифровывать (d)?')
while True:
    command = input('Введите команду (e или d): ')
    if not (command == 'e' or command == 'd'):
        print('Неверная команда. Нужно ввести "e" или "d".')
        continue
    break

text = input('Введите текст: ')

while True:
    offset_s = input('Введите смещение [-25..25]: ')
    if not offset_s.lstrip('-').isdigit():
        print('Смещение должно быть целым числом.')
        continue
    offset = int(offset_s)
    if not -25 <= offset <= 25:
        print('Смещение должно находиться в рамках [-25..25].')
        continue
    break

if command == 'e':
    print('Результат шифровки: ' + encrypt(offset, text))
if command == 'd':
    print('Результат дешифровки: ' + decrypt(offset, text))
