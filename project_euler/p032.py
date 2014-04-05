"""Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

Answer: 45228
"""


from itertools import permutations


def solve():
    digits = [chr(code) for code in range(ord('1'), ord('9') + 1)]
    identities = ([int(''.join(num)) for num in (p[:mult], p[mult:eq], p[:eq])]
                  for p in permutations(digits)
                  for mult in range(1, 8)
                  for eq in range(mult + 1, 9))
    pandigitals = {product for multiplicand, multiplier, product in identities
                   if multiplicand * multiplier == product}
    pandigitals_sum = sum(pandigitals)
    return pandigitals_sum


if __name__ == '__main__':
    print(solve())
