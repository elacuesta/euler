"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


from math import sqrt, ceil

from tools import eratosthenes_sieve


def largest_prime_factor(n):
    root = ceil(sqrt(n))
    sieve = eratosthenes_sieve(root)
    for f in reversed(list(sieve)):
        if n % f == 0:
            return f
    return f


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
