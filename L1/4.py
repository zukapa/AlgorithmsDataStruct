def auth():
    """
    Сложность алгоритма - О(n^2)
    Эффективность алгоритма ниже второй функции потому, что работает перебор
    всех элементов словарей в списке через вложенный цикл for.
    """
    users = [dict(login='user', password='qwerty', activate=True),
             dict(login='super', password='duper', activate=False),
             dict(login='salsa', password='wasabi', activate=False)]
    login = input('Enter your login: ')
    password = input('Enter your password: ')
    stop = 0
    for ind, val in enumerate(users):
        if stop == 0:
            for key, value in val.items():
                if key == 'login' and value == login:
                    stop = 1
                    print('Login correct')
                if key == 'password' and value == password:
                    stop += 1
                    print('Password correct')
                if key == 'activate' and value is True and stop == 2:
                    print('Authorize successfully')
                if key == 'activate' and value is False and stop == 2:
                    activate = input('Your account not activate, activating? (yes): ')
                    if activate == 'yes':
                        users[ind] = dict(login=login, password=password, activate=True)
                    print('Authorize successfully')
    if stop < 2:
        print('Not authorized')


def auth_easy():
    """
    Сложность алгоритма - О(n)
    Эффективность алгоритма выше, чем у первой функции потому, что доступ к элементам
    словаря идет через прямое обращение.
    """
    users = [dict(login='user', password='qwerty', activate=True),
             dict(login='super', password='duper', activate=False),
             dict(login='salsa', password='wasabi', activate=False)]
    login = input('Enter your login: ')
    password = input('Enter your password: ')
    count = 0
    stop = 0
    while count < len(users) and stop == 0:
        if users[count]['login'] == login:
            stop = 1
            print('Login correct')
        if users[count]['password'] == password:
            stop += 1
            print('Password correct')
        if users[count]['activate'] is True and stop == 2:
            print('Authorize successfully')
            break
        if users[count]['activate'] is False and stop == 2:
            activate = input('Your account not activate, activating? (yes): ')
            if activate == 'yes':
                users[count]['activate'] = True
            print('Authorize successfully')
            break
        count += 1
    if stop < 2:
        print('Not authorized')


auth()
auth_easy()
