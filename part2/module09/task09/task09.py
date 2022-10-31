print('Задача 9. Война и мир (необязательная)')


def get_letters_count(file_path: str):
    file = open(file_path, 'r', encoding='utf-8')
    results = dict()
    while True:
        symbol = file.read(1)
        if len(symbol) == 0:
            break
        if not symbol.isalpha():
            continue
        results[symbol] = results.get(symbol, 0) + 1

    return results

# Архива (да и в принципе ничего) не дано поэтому только так.
