from caesar_logic import encrypt, decrypt

print('Добрейший вечерочик. Будем щифровать (e) или расщифровывать (d)?')
s = input('Введите команду: ')
text = input('Введите текст: ')
offset = int(input('Введите смещение: '))
if not -25 <= offset <= 25:
    raise ValueError('Смещение должно находиться в рамках [-25..25].')

if s == 'e':
    print(encrypt(offset, text))
if s == 'd':
    print(decrypt(offset, text))

