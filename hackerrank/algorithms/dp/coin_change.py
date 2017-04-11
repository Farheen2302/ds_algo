def getRecursiveChange(n, arr, index, known):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n > 0 and index == len(arr):
        return 0
    return getRecursiveChange(n - arr[index], arr, index, known) + getRecursiveChange(n, arr, index + 1, known)

assert (getRecursiveChange(10, [2, 5, 3, 6], 0, {})) == 5

# Bottom's up DP approach


def dp_coin_changes(amt, coins):
    result = [[-1 for x in range(amt + 1)] for y in range(len(coins) + 1)]
    for i in range(len(coins) + 1):
        result[i][0] = 1
    for i in range(1, amt + 1):
        result[0][i] = 0
    for i in range(1, len(coins) + 1):
        for j in range(1, amt + 1):
            if coins[i - 1] <= j:
                result[i][j] = result[i - 1][j] + result[i][j - coins[i - 1]]
            else:
                result[i][j] = result[i - 1][j]
    return (result[len(coins)][amt])


assert (dp_coin_changes(5, [1, 2, 3])) == 5
