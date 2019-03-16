from caesar_logic import encrypt, decrypt

print('Добрейший вечерочик. Будем щифровать (e) или расщифровывать (d)?')
s = input('Введите команду: ')
text = input('Введите текст: ')
offset = int(input('Введите смещение: '))

if s == 'e':
    print(encrypt(offset, text))
if s == 'd:':
    print(decrypt(offset, text))

