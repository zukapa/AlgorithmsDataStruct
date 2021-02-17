from random import randint


def median_search(med_list):
    while len(med_list) > 1:
        med_list.remove(min(med_list))
        med_list.remove(max(med_list))
    return med_list[0]


median_list = [randint(-10, 10) for el in range(7)]
print('Random list:', median_list)
print('Median of a random list:', median_search(median_list))
