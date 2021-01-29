import hashlib


def url_caching():
    salt = 'Url'
    url_hash = {'fafad1dbb165d98d77d7bca5e2ae3c37c8037e56af3f833c7bdc9be67e1ef498': 'google.ru',
                'e6629ad9a681163b6cb251415a230efd6a70431c43928d667bb97a1df67c5aff': 'yandex.ru',
                '25bc63b5b655f7a6de5ff873e9167d0d0f4aec433fd023fd5de0ebf1b2024833': 'geekbrains.ru'}
    input_url = input('Enter url: ')
    hash_url = hashlib.sha256(input_url.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    if hash_url in url_hash:
        print('Url located in cache')
    else:
        url_hash[hash_url] = input_url
        print('Url not located in cache. Added.')
    print('\n'.join(url_hash.keys()))


url_caching()
