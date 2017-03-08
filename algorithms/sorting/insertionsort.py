def insertionsort(arr):
	for i in range(1, len(arr)):
		pos = i
		current = arr[i]
		while pos > 0 and arr[pos-1] > current:
			arr[pos] = arr[pos-1]
			pos -= 1
		arr[pos] = current
	return arr

arr = [6,5,4,3,2,1]
assert insertionsort(arr) == [1,2,3,4,5,6]