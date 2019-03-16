def crypt(offset, text):
    if not isinstance(offset, int) or not isinstance(text, str):
        raise TypeError('Неправильный тип аргументов. Нужны int и str.')
    offset %= 26
    result_text = ''
    for symbol in text:
        ord_s = ord(symbol)
        if symbol < 'A' or 'Z' < symbol < 'a' or symbol > 'z':
            result_text += symbol
        else:
            if 'A' <= symbol <= 'Z' < chr(ord_s + offset) or \
                    'a' <= symbol <= 'z' < chr(ord_s + offset):
                result_text += chr(ord_s + offset - 26)
            else:
                result_text += chr(ord_s + offset)
    return result_text


def encrypt(offset, text):
    return crypt(offset, text)


def decrypt(offset, text):
    return crypt(26 - offset, text)

