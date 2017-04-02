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
assert (memo_fibo(10, result)) == 55