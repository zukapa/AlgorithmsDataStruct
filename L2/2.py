def even_odd(number: object, even_count: object, odd_count: object):
    if number == 0:
        number = [el for el in input('Enter number: ')]
    if len(number) == 0:
        print(f'Even and odd numbers: {even_count}, {odd_count}')
    if len(number) != 0:
        extract = int(number.pop(0))
        count = extract % 2
        if count == 0:
            even_count += 1
        if count == 1:
            odd_count += 1
        even_odd(number, even_count, odd_count)


even_odd(0, 0, 0)
