def getRecursiveChange(n, arr, index, known):
	if n == 0:
		return 1
	if index >= len(arr):
		return 0
	key = str(n) + '-' + str(index)
	if key in known.keys():
		return known[key]
	amtWithCoins = 0
	ways = 0
	while amtWithCoins <= n:
		ways += getRecursiveChange(n - amtWithCoins, arr, index + 1, known)
		known[n] = ways
		amtWithCoins += arr[index]
	return ways
 
print(getRecursiveChange(10, [2, 5, 3, 6], 0, {}))
