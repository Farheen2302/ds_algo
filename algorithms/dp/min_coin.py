import sys

# Recursive Solution. Can be optimized by DP


def rec_min_coin(amt, coins):
    if amt == 0:
        return 0
    minimum = sys.maxsize
    for i in coins:
        if i <= amt:
            minimum = min(minimum, rec_min_coin(amt - i, coins) + 1)
    return minimum


assert (rec_min_coin(11, [9, 6, 5, 1])) == 2
