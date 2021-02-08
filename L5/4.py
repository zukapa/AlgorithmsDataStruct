from collections import OrderedDict
from timeit import timeit

usual_dict = {'first': '1', 'second': '2', 'third': '3', 'four': '4'}
ordered_dict = OrderedDict(usual_dict)


def add_usual():
    usual_dict['fifth'] = '5'


def add_ordered():
    ordered_dict['fifth'] = '5'


def remove_usual():
    new_usual = {'first': '1', 'second': '2', 'third': '3', 'four': '4'}
    del new_usual['first']


def remove_ordered():
    new_usual = {'first': '1', 'second': '2', 'third': '3', 'four': '4'}
    new_ordered = OrderedDict(new_usual)
    del new_ordered['first']


print('Time adding element in usual dict:', timeit('add_usual()', globals=globals()))
print('Time adding element in ordered dict:', timeit('add_ordered()', globals=globals()))
print('Time removing element in usual dict:', timeit('remove_usual()', globals=globals()))
print('Time removing element in ordered dict:', timeit('remove_ordered()', globals=globals()))

"""
Временные результаты по функциям:
Time adding element in usual dict: 0.08415600000000001
Time adding element in ordered dict: 0.0991939
Time removing element in usual dict: 0.21724310000000002
Time removing element in ordered dict: 0.8351721000000001

Добавление элемента в обычный словарь эффективнее упорядоченного словаря.
Удаление элемента из обычного словаря эффективнее упорядоченного минимум в 4 раза.
Таким образом, использовать OrderedDict в Python версиях 3.6 и выше не имеет смысла. 
"""
