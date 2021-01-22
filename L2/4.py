def sum_row(quantity, number, summing):
    if quantity == 0:
        print(summing)
    if summing == 0:
        quantity = int(input('Enter number elements: '))
    if quantity > 0:
        return sum_row(quantity - 1, number / (-2), summing=summing + number)


sum_row(1, 1, 0)
