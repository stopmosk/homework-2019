def crypt(offset, text):
    if not isinstance(offset, int) or not isinstance(text, str):
        raise TypeError('Неправильный тип аргументов. Нужны int и str.')
    offset %= 26
    result_text = ''
    for symbol in text:
        ord_s = ord(symbol)
        if ord_s < 65 or 90 < ord_s < 97 or ord_s > 122:
            result_text += symbol
        else:
            if 65 <= ord_s <= 90 < ord_s + offset or \
                    97 <= ord_s <= 122 < ord_s + offset:
                result_text += chr(ord_s + offset - 26)
            else:
                result_text += chr(ord_s + offset)
    return result_text


def encrypt(offset, text):
    return crypt(offset, text)


def decrypt(offset, text):
    return crypt(26 - offset, text)

