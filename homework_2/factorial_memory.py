#from factorial_alg import factor_rec, factor_nonrec
from memory_profiler import profile, memory_usage

# Факториал, рекурсивный вариант
@profile
def factor_rec(num):
    return 1 if num == 0 else num * factor_rec(num - 1)

# Факториал, нерекурсивный вариант
@profile
def factor_nonrec(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(factor_rec(10))
print(factor_nonrec(10))

