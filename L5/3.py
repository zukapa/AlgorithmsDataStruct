from collections import deque
from timeit import timeit
from random import randint


measure_list = ['1', '2']
measure_deque = deque('12')


def add_list():
    measure_list.insert(0, 'Text')


def add_deque():
    measure_deque.appendleft('Text')


def remove_list():
    measure_list.pop(0)


def remove_deque():
    measure_deque.popleft()


def access_list():
    first = measure_list[randint(0, 1)]


def access_deque():
    first = measure_deque[randint(0, 1)]


print('Time adding in beginning to list:', timeit('add_list()', globals=globals(), number=100000))
print('Time adding in beginning to deque:', timeit('add_deque()', globals=globals(), number=100000))
print('Time remove from beginning to list:', timeit('remove_list()', globals=globals(), number=100000))
print('Time remove from beginning to deque:', timeit('remove_deque()', globals=globals(), number=100000))
print('Time access to element in list:', timeit('access_list()', globals=globals(), number=100000))
print('Time access to element in deque:', timeit('access_deque()', globals=globals(), number=100000))

"""
Временные результаты по функциям:
Time adding in beginning to list: 1.7843426
Time adding in beginning to deque: 0.009978599999999949
Time removing from beginning to list: 0.9241351
Time removing from beginning to deque: 0.008420800000000117
Time access to element in list: 0.006718699999999966
Time access to element in deque: 0.007633499999999849

Функции добавляения и удаления в начале списка оказались менее эффективны дека миниммум в 100 раз.
Функция доступа к случайным элементам списка незначительно эффективнее дека.
"""
