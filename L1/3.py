def max_profit():
    """
    Сложность алгоритма - О(n^2).
    Менее эффективный алгоритм, чем во второй функции потому,
    что элементы каждый элемент словаря сравнивается каждым другим значением.
    """
    companies = {'Beverly': 100000,
                 'Folk': 9000,
                 'Umbrella': 50000,
                 'Visit': 400000,
                 'Circus': 80000,
                 'Building': 9000000}
    maximum_profit = {}
    maximum_value = 0
    maximum_key = ''
    while len(companies) > 3:
        for el, val in companies.items():
            for index, value in companies.items():
                if value > val:
                    maximum_value = value
                    maximum_key = index
        maximum_profit[maximum_key] = maximum_value
        del companies[maximum_key]
    print(maximum_profit)


def max_profit_easy():
    """
    Сложность алгоритма - О(N log N).
    Более эффективный алгоритм, чем в первой функции из-за того, что
    результата добиваемся с применением встроенных функций
    и самая трудоемкая из них - sort.
    """
    companies = {'Beverly': 100000,
                 'Folk': 9000,
                 'Umbrella': 50000,
                 'Visit': 400000,
                 'Circus': 80000,
                 'Building': 9000000}

    list_companies = list(companies.items())
    list_companies.sort(key=lambda i: i[1], reverse=True)
    print(list_companies[:-3])


max_profit()
max_profit_easy()
