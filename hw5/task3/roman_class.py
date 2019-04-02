class Roman:
    r_dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6:'VI', 7: 'VII',
              8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL',
              50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C',
              200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC',
              700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M', 0: ''}

    @staticmethod
    def int_to_roman(num):
        Roman.check(num)
        s = str(num)
        # Раскладываем число на степени числа 10
        digits = [int(d) * 10 ** (len(s) - i - 1) for i, d in enumerate(s)]
        result = ''
        for d in digits:
            result += Roman.r_dict[d]
        return result

    @staticmethod
    def check(num):
        if type(num) != int:
            raise TypeError('На входе должно быть целое число')
        if not (0 < num < 2000):
            raise ValueError('Выход за рамки диапазона [1..1999]')

    def __init__(self, num):
        Roman.check(num)
        self.value = num
        self.text = Roman.int_to_roman(num)

    def __str__(self):
        return self.text

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value

    def __add__(self, other):
        result = self.value + other.value
        Roman.check(result)
        return Roman(result)
