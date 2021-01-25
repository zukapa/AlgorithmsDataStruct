import hashlib


def uniq_substring():
    string = input('Enter string: ')
    uniq = []
    hash_string = []
    start = 0
    stop = 1
    while start != len(string) - 1 or stop != len(string) + 1:
        if stop >= 0:
            uniq.append(string[start:stop])
            stop += 1
        if stop == len(string):
            uniq.append(string[start:stop])
            start += 1
            stop = start + 1
    for el in uniq:
        hash_string.append(hashlib.sha256(el.encode('utf-8')).hexdigest())
        if el == string:
            uniq.remove(el)
            hash_string.remove(hashlib.sha256(el.encode('utf-8')).hexdigest())

    uniq_value = set(uniq)
    uniq_hash = set(hash_string)
    print('Uniq substring: ', len(uniq_hash))
    print(', '.join(uniq_value))
    print('\n'.join(uniq_hash))


uniq_substring()
print(hashlib.sha256('geekbrains.ru'.encode('utf-8')).hexdigest())