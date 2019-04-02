import random


sim_len = 1000   # int(input('Введите длину симуляции:'))
chance = 11
test_run = 17
testing_time = 1.5 * 60

random.seed()

for k in range(sim_len):
    result = 'F'
    for i in range(int(testing_time // test_run)):
        s = random.randrange(1, 100)
        if 1 <= s <= chance:
            result = 'L'
            print(result, end='')
            break

    if result == 'L':
        continue

    for i in range(int(testing_time // test_run)):
        s = random.randrange(1, 100)
        if 1 <= s <= chance:
            result = 'S'
            print(result, end='')
            break

    print(result, end='')
