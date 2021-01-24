def ascii_sym(count, element):
    global nextstring
    if count == 127:
        return f'{str(count)} {str(chr(count))}'
    if element % 10 == 0:
        nextstring = f'\n'
    else:
        nextstring = f''
    if count < 127:
        return f'{str(count)} - {str(chr(count))} {nextstring}{str(ascii_sym(count + 1, element + 1))}'


print(ascii_sym(32, 1))
