import random


def show_bug(chance, runs):
    for run in range(runs):
        rnd = random.randrange(1, 100)
        if 1 <= rnd <= chance:
            return True


sim_len = 1000   # int(input('Введите длину симуляции:'))
bug_chance = 11
test_run = 17
testing_time = 1.5 * 60

random.seed()
result = ''

for simulation in range(sim_len):
    print(result, end='')
    result = 'F'

    if show_bug(bug_chance, int(testing_time // test_run)):
        result = 'L'
        continue

    if show_bug(bug_chance, 1):
        result = 'S'
        continue
