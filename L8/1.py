from collections import Counter, deque


def haffman_tree(string):
    global count
    count = Counter(string)
    count_asc = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(count_asc) != 1:
        while len(count_asc) > 1:
            weight = count_asc[0][1] + count_asc[1][1]
            first_elem = (count_asc.popleft()[0], count_asc.popleft()[0])
            for ind, val in enumerate(count_asc):
                if weight > val[1]:
                    continue
                else:
                    count_asc.insert(ind, (first_elem, weight))
                    break
            else:
                count_asc.append((first_elem, weight))
    else:
        weight = count_asc[0][1]
        first_elem = (count_asc.popleft()[0], None)
        count_asc.append((first_elem, weight))
    return count_asc[0][0]


def haffman_code(tree, path=''):
    global code_table
    if path == '':
        code_table = dict()
    if not isinstance(tree, tuple):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


def print_code(string):
    for i in string:
        print(code_table[i], end=' ')


code_string = 'beep boop beer!'
haffman_code(haffman_tree(code_string))
print_code(code_string)

"""
Изменены имена переменных на более точные. Дерево теперь строится из более экономичного по памяти кортежа. 
Создана отдельная функция для печати закодированной строки. Глобальные переменные перенесены в функции. 
"""
