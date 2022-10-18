print('Задача 2. Универсальная программа 2')


def gen_primes(max_excluded: int = None):
    not_primes = dict()
    current = 2

    while max_excluded is None or current < max_excluded:
        if current in not_primes:
            for prime_divider in not_primes[current]:
                not_primes.setdefault(current + prime_divider, []).append(prime_divider)
            del not_primes[current]
        else:
            yield current
            not_primes[current * current] = [current]

        current += 1


def crypto(source):
    return [source[prime] for prime in gen_primes(len(source))]


test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'{test}:\n{crypto(test)}')

test = 'О Дивный Новый мир!'
print(f'{test}:\n{crypto(test)}')
