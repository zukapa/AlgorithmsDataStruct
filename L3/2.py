import hashlib


def auth():
    base = {}
    salt = 'Hash is good'
    password = input('Enter your password: ')
    hash_password = hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    print('Hash first enter:', hash_password)
    base['password'] = hash_password
    password_again = input('Enter your password, again: ')
    hash_password_again = hashlib.sha256(password_again.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    if hash_password_again == base['password']:
        print('Passwords coincide')
    else:
        print('Passwords not coincide')
    print('Hash second enter:', hash_password_again)


auth()
