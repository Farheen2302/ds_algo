
def sequential(item, arr):
	found = False
	for i in arr:
		if i == item:
			found = True
	return found

# Divide and Conquer
# With slice operator in python, binary search does not takes place in O(logn) time. Avoid this by passing start,end
def binary(item, arr):
	if len(arr) == 0:
		return False
	else:
		mid = len(arr) // 2
		if item == arr[mid]:
			return True
		else:
			if item > arr[mid]:
				return binary(item, arr[mid+1:])
			else:
				return binary(item, arr[:mid])

#Test Cases
arr = [45,67,3,2,8,-4,5,2,87]
assert sequential(64, arr) == False
assert sequential(-4, arr) == True
arr.sort()
assert binary(67, arr) == True
assert binary(88, arr) == False