from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

"""
Время выполнения функции без мемоизации при 10000 повторах:
0.019483299999999995 (случайное число от 10000 до 1000000)
0.021360699999999996 (случайное число от 1000000 до 10000000)
0.03867770000000001 (случайное число от 10000000 до 10000000000000)

Время выполнения функции с мемоизацией при 10000 повторах:
0.001430600000000004 (случайное число от 10000 до 1000000)
0.0014631000000000088 (случайное число от 1000000 до 10000000)
0.001521400000000006 (случайное число от 10000000 до 10000000000000)

Проанализировав время выполнения можно понять, что время выполнения 
уменьшилось в 100 и больше раз и почти пропала зависимость времени 
выполнения от величины числа.
Мемоизация в этой функции эффективна потому, что при построении обратного 
числа используемые цифры с большой вероятностью будут повторяться.
"""
