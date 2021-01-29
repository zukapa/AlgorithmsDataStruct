from cProfile import run
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


run('revers_1(123456789)')
run('revers_2(123456789)')
run('revers_3(123456789)')
print(timeit('revers_1(123456789)', globals=globals()))
print(timeit('revers_2(123456789)', globals=globals()))
print(timeit('revers_3(123456789)', globals=globals()))

"""
Первая функция получила результат профилирования:
13 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     10/1    0.000    0.000    0.000    0.000 3.py:19(revers_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
И время выполнения на 1 млн. повторах:
1.8385983

Вторая функция получила результат профилирования:
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 3.py:29(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

И время выполнения на 1 млн. повторах:
1.2232191000000001

Третья функция получила результат профилирования:
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 3.py:37(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

И время выполнения на 1 млн. повторах:
0.2744759000000001

Первая функция выполнялась дольше остальных потому, что реализация через рекурсию практически всегда
наиболее затратна по ресурсам из-за стека вызовов (стек из 10 вызовов, можно увидеть в результате профилирования).
Вторая функция эффективнее первой, но не третьей потому, что используется цикл и извлекается
по одной цифре за итерцию.
Третья функция наиболее эффективная потому, что используется срез с шагом -1. Это значит, что пробегаться по 
числу не нужно, как в цикле. Срез сразу дает в результате число обратное числу на входе.
"""
