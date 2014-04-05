"""Coin sums

In England the currency is made up of pound and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, 1 pound (100p) and 2 pound (200p).

It is possible to make 2 pound in the following way:

    1 * 1 pound + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can 2 pound be made using any number of coins?

Answer: 73682
"""


from collections import deque


def solve():
    COINS = [200, 100, 50, 20, 10, 5, 2, 1]
    states = deque([(200, 0)])
    size = len(COINS)
    count = 0

    while states:
        state = states.pop()

        for i in range(state[1], size):
            c = COINS[i]
            target = state[0] - c
            if target == 0:
                count += 1
            elif target > 0:
                states.append((target, i))

    return count


if __name__ == '__main__':
    print(solve())
