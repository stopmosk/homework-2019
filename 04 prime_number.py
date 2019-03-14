def is_prime(num):
    if num == 1:
        return 'Число очень сложное'
    if num == 2:
        return 'Число простое'
    for div in range(2, num):
        if num % div == 0:
            return 'Число совсем не такое простое, как кажется'
        return 'Число простое'


print(is_prime(int(input())))
