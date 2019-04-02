import random


def show_bug(chance):
    rnd = random.randrange(1, 100)
    if 1 <= rnd <= chance:
        return True


sim_len = 1000   # int(input('Введите длину симуляции:'))
bug_chance = 11
test_run = 17
testing_time = 1.5 * 60

random.seed()

result = ''
for k in range(sim_len):
    print(result, end='')
    result = 'F'

    for i in range(int(testing_time // test_run)):
        if show_bug(bug_chance):
            result = 'L'
            break
    if result == 'L':
        continue
    if show_bug(bug_chance):
        result = 'S'
        continue
