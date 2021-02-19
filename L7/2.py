import timeit
import random


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


float_list = [random.uniform(0, 50) for _ in range(10)]
print('Исходный список на 10 элементов:', float_list)
print('Временной результат при 10 элементах:',
      timeit.timeit(
          "merge_sort(float_list)",
          globals=globals(),
          number=1000))
print('Отсортированный список на 10 элементов:', float_list)
float_list = [random.uniform(0, 50) for _ in range(100)]
print('Исходный список на 100 элементов:', float_list)
print('Временной результат при 100 элементах:',
      timeit.timeit(
          "merge_sort(float_list)",
          globals=globals(),
          number=1000))
print('Отсортированный список на 10 элементов:', float_list)
float_list = [random.uniform(0, 50) for _ in range(1000)]
print('Исходный список на 100 элементов:', float_list)
print('Временной результат при 1000 элементах:',
      timeit.timeit(
          "merge_sort(float_list)",
          globals=globals(),
          number=1000))
print('Отсортированный список на 10 элементов:', float_list)
