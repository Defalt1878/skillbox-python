print('Задача 3. Криптовалюта')

data = {
    'address': '0x544444444444',
    'ETH': {
        'balance': 444,
        'totalIn': 444,
        'totalOut': 4
    },
    'count_txs': 2,
    'tokens': [
        {
            'fst_token_info': {
                'address': '0x44444',
                'name': 'fdf',
                'decimals': 0,
                'symbol': 'dsfdsf',
                'total_supply': '3228562189',
                'owner': '0x44444',
                'last_updated': 1519022607901,
                'issuances_count': 0,
                'holders_count': 137528,
                'price': False
            },
            'balance': 5000,
            'totalIn': 0,
            'total_out': 0
        },
        {
            'sec_token_info': {
                'address': '0x44444',
                'name': 'ggg',
                'decimals': '2',
                'symbol': 'fff',
                'total_supply': '250000000000',
                'owner': '0x44444',
                'last_updated': 1520452201,
                'issuances_count': 0,
                'holders_count': 20707,
                'price': False
            },
            'balance': 500,
            'totalIn': 0,
            'total_out': 0
        }
    ]
}

# 1. Вывести списки ключей и значений словаря.
print(list(data.keys()))
print(list(data.values()))

# 2. В “ETH” добавить ключ “total_diff” со значением 100.
data['ETH']['total_diff'] = 100

# 3. Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
data['tokens'][0]['fst_token_info']['name'] = 'doge'

# 4. Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
data['ETH']['total_out'] = sum([token['total_out'] for token in data['tokens']])

# 5. Внутри "sec_token_info" изменить название ключа “price” на “total_price”.
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
