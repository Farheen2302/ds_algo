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


def memo_min_coin(amt, coins, result):
    if amt in result:
        return result[amt]
    minimum = sys.maxsize
    for i in coins:
        if i <= amt:
            minimum = min(minimum, memo_min_coin(amt - i, coins, result) + 1)
    result[amt] = minimum
    return minimum

assert (memo_min_coin(11, [9, 6, 5], {0: 0})) == 2
assert  (rec_min_coin(3, [9, 6, 5, 1]))  == 3
