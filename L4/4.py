from timeit import timeit


array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    elem = max(set(array), key=array.count)
    return f'Чаще всего появилось число {elem}'


print(timeit('func_1', globals=globals(), number=10000000))
print(timeit('func_2', globals=globals(), number=10000000))
print(timeit('func_3', globals=globals(), number=10000000))

"""
Время выполнения первой функции при 10000000 повторах: 0.1748132
Время выполнения первой функции при 10000000 повторах: 0.1829223
Время выполнения первой функции при 10000000 повторах: 0.15270050000000002

Эффективнее всего получилась третья функция потому, что используем 
встроенные функции set и max, а они оптимизированны под меньшее время 
выполнения.
Время выполнения первых двух функций приблизительно одинаково потому, 
что в обоих случаях используем перебор всего списка через цикл for.
"""
