# Refer : http://www.geeksforgeeks.org/g-fact-18/
import time


def get_bin_tree(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += get_bin_tree(i) * get_bin_tree(n - i - 1)
    return res

# Memoization approach


def memo_get_bin_tree(n, result):
    if n <= 1:
        return 1
    res = 0
    if n in result:
        return result[n]
    for i in range(n):
        res += memo_get_bin_tree(i, result) * \
            memo_get_bin_tree(n - i - 1, result)
    result[n] = res
    return res


start_time = time.time()
print(get_bin_tree(15))
print("--- %s Recursive seconds ---" % (time.time() - start_time))
start_time = time.time()
print(memo_get_bin_tree(15, {}))
print("--- %s DP seconds ---" % (time.time() - start_time))
