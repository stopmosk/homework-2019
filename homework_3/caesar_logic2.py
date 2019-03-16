def check_args(offset, text):
    if not isinstance(offset, int) or not isinstance(text, str):
        raise TypeError('Неправильный тип аргументов. Нужны int и str.')
    if offset < 0 or offset > 25:
        raise ValueError('Смещение должно находиться в рамках [0..25].')


def crypt(offset, text):
    check_args(offset, text)
    result_text = ''
    for symbol in text:
        ord_s = ord(symbol)
        if 65 <= ord_s <= 90 < ord_s + offset or 97 <= ord_s <= 122 < ord_s + offset:
            offset -= 26
        if ord_s < 65 or 90 < ord_s < 97 or ord_s > 122:
            raise ValueError('Строка на входе должна состоять только из символов a..z и A..Z')
        result_text += chr(ord_s + offset)
    return result_text


def encrypt(offset, text):
    check_args(offset, text)
    return crypt(offset, text)


def decrypt(offset, text):
    check_args(offset, text)
    return crypt(26 - offset, text)

# print(encrypt(1, 'aAbBcCxXyYzZ'))
# print(decrypt(1, 'aAbBcCxXyYzZ'))
