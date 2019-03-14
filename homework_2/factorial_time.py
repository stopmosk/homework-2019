from factorial_alg import factor_rec, factor_nonrec
import timeit

def compars_fn(rng, attempts):
    print('Отношение времени рекурсивного и нерекурсивного алгоритмов при ' + str(attempts) + ' попыток:')
    for n in rng:
        print(n, end=' ')
        time_r, time_nr = 0, 0
        for j in range(attempts):
            start = timeit.default_timer()
            factor_rec(n)
            time_r += (timeit.default_timer() - start) / attempts

            start = timeit.default_timer()
            factor_nonrec(n)
            time_nr += (timeit.default_timer() - start) / attempts

        print(time_r / time_nr)

compars_fn(range(1, 10), 1000000)
compars_fn(range(10, 101, 10), 100000)
compars_fn(range(100, 901, 100), 10000)
