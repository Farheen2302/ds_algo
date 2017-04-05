import sys

# Recursive Solution. Can be optimized by DP

# Note: Integer overflow should also be taken care of if written in other
# languages like java etc


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


def bottoms_up(amt, coins, result):
	result[0] = 0
	for i in range(1, amt + 1):
		minimum = sys.maxsize
		for j in coins:
			if j <= i:
				minimum = min(minimum, result[i - j])
			if minimum != sys.maxsize:
				result[i] = minimum + 1
			else:
				result[i] = sys.maxsize
	return result[amt]


assert (memo_min_coin(11, [9, 6, 5], {0: 0})) == 2
assert (rec_min_coin(3, [9, 6, 5, 1])) == 3
assert (bottoms_up(11, [9, 6, 5], [0]*12)) == 2
assert (bottoms_up(63, [1,5,10,21,25], [0]*64)) == 3
