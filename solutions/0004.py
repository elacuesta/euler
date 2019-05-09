"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    return list(str(n)) == list(reversed(str(n)))


def palindrome(factor_length=2):
    a = 10**factor_length - 1
    b = 10**factor_length - 1
    while True:
        p = a * b
        if is_palindrome(p):
            return p, a, b
        a -= 1
        p = a * b
        if is_palindrome(p):
            return p, a, b


if __name__ == '__main__':
    print(palindrome(3))
