import time


def fill_list():
    """
    Список заполняется быстрее, так как число элементов меньше,
    чем в словаре (не нужно вычислять ключи или индексы) и нет вычислений хеша для ключей.
    """
    start = time.time()
    [el for el in range(1000000)]
    end = time.time()
    return end - start


def fill_dict():
    """
    Словарь заполняется медленнее, так как число элементов больше,
    чем в списке (нужно вычислять ключи отдельно) и вычисляется хеш для ключей.
    """
    start = time.time()
    {el: el for el in range(1000000)}
    end = time.time()
    return end - start


def addiction_list():
    """
    Добавление элемента в список работает быстрее словаря потому, что
    нет вычислений хеша и не нужно записывать индексы.
    """
    gen_list = []
    count = 0
    start = time.time()
    while count < 10000000:
        gen_list.append(count)
        count += 1
    end = time.time()
    return end - start


def addiction_dict():
    """
    Добавление элемента в словарь работает медленнее списка потому, что
    вычисленяются хеши для ключей и ключи нужно записывать отдельно.
    """
    gen_dict = {}
    count = 0
    start = time.time()
    while count < 10000000:
        gen_dict[f'{count}'] = count
        count += 1
    end = time.time()
    return end - start


def removal_list():
    """
    Удаление элемента списка производится медленнее потому, что
    используется поиск элемента по значению и сложность операции
    имеет линейную зависимость от количества элементов.
    """
    gen_list = [el for el in range(100000)]
    count = 0
    start = time.time()
    while len(gen_list) != 0:
        gen_list.remove(count)
        count += 1
    end = time.time()
    return end - start


def removal_dict():
    """
    Удаление элемента словаря производится быстрее потому, что
    поиск элемента работает эфеективнее и не зависит от количества элементов.
    """
    gen_dict = {el: el for el in range(100000)}
    count = 0
    start = time.time()
    while count < 100000:
        del gen_dict[count]
        count += 1
    end = time.time()
    return end - start


print('Время построения списка:', fill_list())
print('Время построения словаря:', fill_dict())
print('Время добавления элемента в список:', addiction_list())
print('Время добавления элемента в словарь:', addiction_dict())
print('Время удаления элемента из списка:', removal_list())
print('Время удаления элемента из словаря:', removal_dict())
