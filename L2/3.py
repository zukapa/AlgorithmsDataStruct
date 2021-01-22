def reverse(number: object, reverse_number: object):
    if number == 0:
        number = [el for el in input('Enter number: ')]
        reverse_number = []
    if len(number) == 0:
        print(f'Reverse number:', ''.join(map(str, reverse_number)))
    if len(number) != 0:
        extract = int(number.pop(len(number) - 1))
        reverse_number.append(extract)
        reverse(number, reverse_number)


reverse(0, 0)
