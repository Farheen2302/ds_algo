def bubblesort(arr):
	maxi = len(arr)
	for i in range(0, maxi-1):
		for j in range((len(arr))-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
		maxi -= 1
	return arr

arr = [6,5,4,3,2,1]
assert bubblesort(arr) == [1,2,3,4,5,6]
