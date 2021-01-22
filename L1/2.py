# Сложность алгоритма - О(n^2)
def min_element():
    list_min = [8, 2, 3, 4, 5, 1, 7, 8, 9, 10]
    minimum = float("inf")
    for el in list_min:
        for val in list_min:
            if el < val:
                if minimum > el:
                    minimum = el
    print(minimum)


# Сложность алгоритма - О(n)
def min_element_easy():
    list_min = [el for el in range(1, 11)]
    minimum = min(list_min)
    print(minimum)
