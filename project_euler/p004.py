"""Largest palindrome product

A palindromic number reads the same both ways.

The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
"""


def solve():
    maxProduct = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if (product > maxProduct and
                    product % 10 == product // 100000 and
                    (product % 100) // 10 == (product % 100000) // 10000 and
                    (product % 1000) // 100 == (product % 10000) // 1000):
                maxProduct = product
    return maxProduct


if __name__ == '__main__':
    print(solve())
