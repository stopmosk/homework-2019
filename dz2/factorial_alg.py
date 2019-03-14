# Факториал, рекурсивный вариант
def factor_rec(num):
    return 1 if num == 0 else num * factor_rec(num - 1)

# Факториал, нерекурсивный вариант
def factor_nonrec(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
