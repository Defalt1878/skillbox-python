import math
import sys
import time

print('Задача 3. Читабельность кода')


def gen_primes(max_excluded: int = sys.maxsize):
    not_primes = dict()
    current = 2

    while current < max_excluded:
        if current in not_primes:
            for prime_divider in not_primes[current]:
                not_primes.setdefault(current + prime_divider, []).append(prime_divider)
            del not_primes[current]
        else:
            yield current
            not_primes[current * current] = [current]

        current += 1


start = time.time()
print(list(gen_primes(100000)))
print((time.time() - start) * 1000)  # 35 ms

start = time.time()
print(list(filter(
    lambda x: x == 2 or x % 2 != 0 and all(map(lambda y: x % y != 0, range(3, int(math.sqrt(x)) + 1, 2))),
    range(2, 100000)
)))
print((time.time() - start) * 1000)  # 115 ms
