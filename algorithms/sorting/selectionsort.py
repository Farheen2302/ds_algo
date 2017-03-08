def selectionsort(arr):
	for i in range(len(arr)-1, 0, -1):
		short = 0
		for j in range(1, i+1):
			if arr[j] > arr[short]:
				short = j
		arr[short], arr[i] = arr[i], arr[short]
	return arr

arr = [7,6,5,4,3,2,1,7]
assert selectionsort(arr) == [1,2,3,4,5,6,7,7]

