from memory_profiler import profile
from recordclass import recordclass
from collections import namedtuple
import numpy


@profile
def min_element_easy():
    list_min = [el for el in range(1, 100000)]
    minimum = min(list_min)
    print(minimum)


"""
Результаты профилирования памяти базовой функции поиска минимального элемента:
Filename: 1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     32.0 MiB     32.0 MiB           1   @profile
    29                                         def min_element_easy():
    30     36.0 MiB      4.0 MiB      100002       list_min = [el for el in range(1, 100000)]
    31     36.0 MiB      0.0 MiB           1       minimum = min(list_min)
    32     36.0 MiB      0.0 MiB           1       print(minimum)

Декоратор @profile потребляет 32 мебибайта. 
Списковое включение потребляет 4 мебибайта.
Следующие строки кода потребяют незначительно памяти.
"""


@profile
def min_element_tuple():
    tuple_min = (el for el in range(1, 100000))
    minimum = min(tuple_min)
    print(minimum)


"""
Результаты профилирования памяти улучшенной функции поиска минимального элемента:
Filename: 1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     32.0 MiB     32.0 MiB           1   @profile
    36                                         def min_element_tuple():
    37     32.0 MiB      0.0 MiB      200001       tuple_min = (el for el in range(1, 100000))
    38     32.0 MiB      0.0 MiB           1       minimum = min(tuple_min)
    39     32.0 MiB      0.0 MiB           1       print(minimum)
    
В данном случае уменьшилось потребление памяти за счет замены 
создания списка на кортеж до незначительного значения.
"""


@profile
def min_element_numpy():
    numpy_min = numpy.array([el for el in range(1, 100000)])
    minimum = min(numpy_min)
    print(minimum)


"""
Результаты профилирования памяти улучшенной функции поиска минимального элемента:
Filename: 1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     32.0 MiB     32.0 MiB           1   @profile
    43                                         def min_element_numpy():
    44     36.4 MiB      1.7 MiB      100002       numpy_min = numpy.array([el for el in range(1, 100000)])
    45     33.7 MiB     -2.7 MiB           1       minimum = min(numpy_min)
    46     33.7 MiB      0.0 MiB           1       print(minimum)

Использован другой способ уменьшить потребляемую память - массив библиотеки NumPy.
"""


@profile
def dict_profile():
    dict_prof = {el: el for el in range(100000)}
    return dict_prof


"""
Результаты профилирования памяти функции наполнения словаря:
Filename: 1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   102     32.4 MiB     32.4 MiB           1   @profile
   103                                         def dict_profile():
   104     40.4 MiB      8.1 MiB      100003       dict_prof = {el: el for el in range(100000)}
   105     40.4 MiB      0.0 MiB           1       return dict_prof

Функция наполнения 100000 элементами словаря требует 8,1 мебибайт.
"""


@profile
def record_profile():
    record_prof = recordclass('profile', 'key value')
    for el in range(100000):
        globals()[f'ep_{el}'] = record_prof(el, el)
    return record_prof


"""
Результаты профилирования памяти функции создания объектов через recordclass:
Filename: 1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   108     33.0 MiB     33.0 MiB           1   @profile
   109                                         def record_profile():
   110     33.0 MiB      0.0 MiB           1       record_prof = recordclass('profile', 'key value')
   111     51.3 MiB      1.5 MiB      100001       for el in range(100000):
   112     51.3 MiB     16.8 MiB      100000           globals()[f'ep_{el}'] = record_prof(el, el)
   113     51.3 MiB      0.0 MiB           1       return record_prof

Функция создания 100000 объектов через recordclass требует 16,8 мебибайт, что менее эффективно, чем
в предыдущей функции наполнения словаря.
"""


@profile
def tuple_profile():
    tuple_prof = namedtuple('profile', 'key value')
    for el in range(100000):
        globals()[f'ep_{el}'] = tuple_prof(el, el)
    return tuple_prof


"""
Результаты профилирования памяти функции создания объектов через коллекцию namedtuple:
Filename: 1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   116     51.3 MiB     51.3 MiB           1   @profile
   117                                         def tuple_profile():
   118     51.3 MiB      0.0 MiB           1       tuple_prof = namedtuple('profile', 'key value')
   119     52.8 MiB      0.0 MiB      100001       for el in range(100000):
   120     52.8 MiB      1.5 MiB      100000           globals()[f'ep_{el}'] = tuple_prof(el, el)
   121     52.8 MiB      0.0 MiB           1       return tuple_prof

Функция создания 100000 объектов через коллекцию namedtuple требует 1,5 мебибайт, тем самым, она
эффективнее двух предыдущих реализаций.
"""


@profile
def max_profit_easy():
    companies = {'Beverly': 100000,
                 'Folk': 9000,
                 'Umbrella': 50000,
                 'Visit': 400000,
                 'Circus': 80000,
                 'Building': 9000000}
    list_companies = list(companies.items())
    list_companies.sort(key=lambda i: i[1], reverse=True)
    print(list_companies[:-3])


"""
Результаты профилирования памяти функции поиска трех наиболее прибыльных компаний через словарь:
Filename: 1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   172     32.7 MiB     32.7 MiB           1   @profile
   173                                         def max_profit_easy():
   174     32.7 MiB      0.0 MiB           2       companies = {'Beverly': 100000,
   175     32.7 MiB      0.0 MiB           1                    'Folk': 9000,
   176     32.7 MiB      0.0 MiB           1                    'Umbrella': 50000,
   177     32.7 MiB      0.0 MiB           1                    'Visit': 400000,
   178     32.7 MiB      0.0 MiB           1                    'Circus': 80000,
   179     32.7 MiB      0.0 MiB           1                    'Building': 9000000}
   180     32.7 MiB      0.0 MiB           1       list_companies = list(companies.items())
   181     32.7 MiB      0.0 MiB          13       list_companies.sort(key=lambda i: i[1], reverse=True)
   182     32.7 MiB      0.0 MiB           1       print(list_companies[:-3])
   
Проанализировав результаты профилирования памяти можно сказать, что сделать вывод по эффективности можно 
при большем количестве элементов.
Реализация через словарь - средняя по эффективности, проанализировав предыдущую функцию наполнения словаря.
"""


@profile
def max_profit_record():
    list_companies = []
    companies = recordclass('companies', 'name profit')
    first = companies('Beverly', 100000)
    second = companies('Folk', 9000)
    third = companies('Umbrella', 50000)
    fourth = companies('Visit', 400000)
    fifth = companies('Circus', 80000)
    sixth = companies('Building', 9000000)
    list_companies.append(first.profit)
    list_companies.append(second.profit)
    list_companies.append(third.profit)
    list_companies.append(fourth.profit)
    list_companies.append(fifth.profit)
    list_companies.append(sixth.profit)
    list_companies.sort(reverse=True)
    print(list_companies[:-3])


"""
Результаты профилирования памяти функции поиска трех наиболее прибыльных компаний через recordclass:
Filename: 1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   190     32.7 MiB     32.7 MiB           1   @profile
   191                                         def max_profit_record():
   192     32.7 MiB      0.0 MiB           1       list_companies = []
   193     32.7 MiB      0.0 MiB           1       companies = recordclass('companies', 'name profit')
   194     32.7 MiB      0.0 MiB           1       first = companies('Beverly', 100000)
   195     32.7 MiB      0.0 MiB           1       second = companies('Folk', 9000)
   196     32.7 MiB      0.0 MiB           1       third = companies('Umbrella', 50000)
   197     32.7 MiB      0.0 MiB           1       fourth = companies('Visit', 400000)
   198     32.7 MiB      0.0 MiB           1       fifth = companies('Circus', 80000)
   199     32.7 MiB      0.0 MiB           1       sixth = companies('Building', 9000000)
   200     32.7 MiB      0.0 MiB           1       list_companies.append(first.profit)
   201     32.7 MiB      0.0 MiB           1       list_companies.append(second.profit)
   202     32.7 MiB      0.0 MiB           1       list_companies.append(third.profit)
   203     32.7 MiB      0.0 MiB           1       list_companies.append(fourth.profit)
   204     32.7 MiB      0.0 MiB           1       list_companies.append(fifth.profit)
   205     32.7 MiB      0.0 MiB           1       list_companies.append(sixth.profit)
   206     32.7 MiB      0.0 MiB           1       list_companies.sort(reverse=True)
   207     32.7 MiB      0.0 MiB           1       print(list_companies[:-3])
   
Проанализировав результаты профилирования памяти можно сказать, что сделать вывод по эффективности можно 
при большем количестве элементов.
Реализация через recordclass - наихудшая по эффективности, проанализировав предыдущую функцию создания 
объектов recordclass.
"""


@profile
def max_profit_tuple():
    list_companies = []
    companies = namedtuple('companies', 'name profit')
    first = companies('Beverly', 100000)
    second = companies('Folk', 9000)
    third = companies('Umbrella', 50000)
    fourth = companies('Visit', 400000)
    fifth = companies('Circus', 80000)
    sixth = companies('Building', 9000000)
    list_companies.append(first.profit)
    list_companies.append(second.profit)
    list_companies.append(third.profit)
    list_companies.append(fourth.profit)
    list_companies.append(fifth.profit)
    list_companies.append(sixth.profit)
    list_companies.sort(reverse=True)
    print(list_companies[:-3])


"""
Результаты профилирования памяти функции поиска трех наиболее прибыльных компаний используя 
коллекцию namedtuple:
Filename: 1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   210     32.7 MiB     32.7 MiB           1   @profile
   211                                         def max_profit_tuple():
   212     32.7 MiB      0.0 MiB           1       list_companies = []
   213     32.7 MiB      0.0 MiB           1       companies = namedtuple('companies', 'name profit')
   214     32.7 MiB      0.0 MiB           1       first = companies('Beverly', 100000)
   215     32.7 MiB      0.0 MiB           1       second = companies('Folk', 9000)
   216     32.7 MiB      0.0 MiB           1       third = companies('Umbrella', 50000)
   217     32.7 MiB      0.0 MiB           1       fourth = companies('Visit', 400000)
   218     32.7 MiB      0.0 MiB           1       fifth = companies('Circus', 80000)
   219     32.7 MiB      0.0 MiB           1       sixth = companies('Building', 9000000)
   220     32.7 MiB      0.0 MiB           1       list_companies.append(first.profit)
   221     32.7 MiB      0.0 MiB           1       list_companies.append(second.profit)
   222     32.7 MiB      0.0 MiB           1       list_companies.append(third.profit)
   223     32.7 MiB      0.0 MiB           1       list_companies.append(fourth.profit)
   224     32.7 MiB      0.0 MiB           1       list_companies.append(fifth.profit)
   225     32.7 MiB      0.0 MiB           1       list_companies.append(sixth.profit)
   226     32.7 MiB      0.0 MiB           1       list_companies.sort(reverse=True)
   227     32.7 MiB      0.0 MiB           1       print(list_companies[:-3])

Проанализировав результаты профилирования памяти можно сказать, что сделать вывод по эффективности можно 
при большем количестве элементов.
Реализация, используя коллекцию namedtuple - наилучшая по эффективности, проанализировав предыдущую функцию 
создания объектов коллекции namedtuple.
"""


min_element_easy()
min_element_tuple()
min_element_numpy()
dict_profile()
record_profile()
tuple_profile()
max_profit_easy()
max_profit_record()
max_profit_tuple()
