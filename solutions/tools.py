from math import sqrt, floor


def eratosthenes_sieve(n):
    """
    Based on http://stackoverflow.com/questions/19345627/
    """
    sieve = list(range(n + 1))
    sieve[0], sieve[1] = False, False
    for i in range(2, int(floor(sqrt(n))) + 1):
        if sieve[i]:
            sieve[i**2: n+1: i] = [False] * len(range(i**2, n+1, i))
    return filter(None, sieve)


def prime_factors(n):
    sieve = eratosthenes_sieve(n)
    while n > 1:
        try:
            f = next(sieve)
        except StopIteration:
            return
        while n % f == 0:
            yield f
            n = n / f
