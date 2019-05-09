"""
https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_multiples(n=10, factors=(3, 5)):
    result = 0
    for i in range(n):
        for f in factors:
            if i % f == 0:
                result += i
                break
    return result


if __name__ == '__main__':
    for n in [10, 100, 1000]:
        print('n={}, result={}'.format(n, sum_multiples(n)))
