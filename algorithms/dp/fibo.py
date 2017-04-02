# DP with memoization

def memo_fibo(n, result):
	if n in result.keys():
		return result[n]
	else:
		result[n] = memo_fibo(n-1, result) + memo_fibo(n-2, result)
		return result[n]
result = {
	0: 0,
	1: 1
}


# But sometimes, it's better to go for bottom's up

def dp_bu_fibo(n):
	result = {0: 0, 1: 1}
	for i in range(2, n+1):
		result[i] = result[i-1] + result[i-2]
	return result[n]

assert (memo_fibo(10, result)) == 55
assert dp_bu_fibo(10) == 55