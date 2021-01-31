from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """
    Оптимизированная функция, повторающая результат первой функции, но
    работающая за меньшее время за счет спискового включения.
    Списковое включение эффективнее потому, что она является встроенным механизмом
    генерации списков.
    """
    even = [v for v in range(len(nums)) if v % 2 == 0]
    return even


print(timeit('func_1([el for el in range(10)])', globals=globals()))
print(timeit('func_2([el for el in range(10)])', globals=globals()))

"""
Результаты замеров времени выполнения на 1 млн. повторах:
func_1 = 1.4177823
func_2 = 1.2867255
"""
