def calc():
    operator = input('Enter operator(+, -, *, /. For exit - 0): ')
    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))
    if operator == '0':
        print('The end!')
    if second == 0 and operator == '/':
        print('Cannot divide by zero. After exit you see exception ZeroDivisionError')
        calc()
    if operator == '+':
        print(f'{first + second}')
        calc()
    if operator == '-':
        print(f'{first - second}')
        calc()
    if operator == '*':
        print(f'{first * second}')
        calc()
    if operator == '/':
        print(f'{first / second}')
        calc()
    if operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '0':
        print('Please, enter correct operator')
        calc()


calc()
