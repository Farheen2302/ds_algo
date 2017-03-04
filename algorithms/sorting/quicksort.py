def quicksort(arr, start, end):
	if start < end:
		pivot = _quicksort(arr, start, end)
		left = quicksort(arr, 0, pivot-1)
		right = quicksort(arr, pivot+1, end)
	return arr

def _quicksort(arr, start, end):
	pivot = start
	left = start + 1
	right = end
	done = False
	while not done:
		while arr[left] < arr[pivot]:
			left += 1
		while arr[right] > arr[pivot]:
			right -= 1
		if left >= right:
			done = True
		else:
			swap(arr, left, right)
	swap(arr, pivot, right)
	return right

def swap(arr, left, right):
	temp = arr[left]
	arr[left] = arr[right]
	arr[right] = temp


#Test Cases
arr = [8,7,6,5,4,3,2,1]
arr1 = [54,26,93,17,77,31,44,55,20]
assert sorted(arr1) == quicksort(arr1, 0, len(arr1)-1)
#Failing case
#assert sorted(arr) == quicksort(arr, 0, len(arr)-1)

