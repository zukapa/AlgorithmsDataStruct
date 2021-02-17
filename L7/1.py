import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_smart(lst_obj):
    n = 1
    control_lst = lst_obj.copy()
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if control_lst == lst_obj:
            break
        n += 1
    return lst_obj


first_list = [random.randint(-100, 100) for _ in range(100)]
second_list = first_list.copy()
print(first_list)
bubble_sort(first_list)
print(first_list)
print('Временной результат неулучшенной функции пузырьковой сортировки отсортированного списка:',
      timeit.timeit(
          "bubble_sort(first_list[:])",
          globals=globals(),
          number=1000))

print('Временной результат неулучшенной функции пузырьковой сортировки неотсортированного списка:',
      timeit.timeit(
          "bubble_sort(second_list[:])",
          globals=globals(),
          number=1000))

print('Временной результат улучшенной функции пузырьковой сортировки отсортированного списка:',
      timeit.timeit(
          "bubble_smart(first_list[:])",
          globals=globals(),
          number=1000))

print('Временной результат улучшенной функции пузырьковой сортировки неотсортированного списка:',
      timeit.timeit(
          "bubble_smart(second_list[:])",
          globals=globals(),
          number=1000))


"""
Результаты замеров:
Временной результат неулучшенной функции пузырьковой сортировки отсортированного списка: 0.3292927
Временной результат неулучшенной функции пузырьковой сортировки неотсортированного списка: 0.5183367999999999
Временной результат улучшенной функции пузырьковой сортировки отсортированного списка: 0.005855600000000072
Временной результат улучшенной функции пузырьковой сортировки неотсортированного списка: 0.5588534

Сравнивая временные результаты сортировки отсортированного списка:  
0.3292927 (неулучшенная функция) и 0.005855600000000072 (улучшенная функция), можно утверждать, что оптмизация
эффективна.

Улучшение функции пузырьковой сортировки состоит в добавлении условия сравнения списка на входе со списком после
первого прохождения через цикл for - если списки равны, то выходим из цикла while и завершаем работу функции.
"""
