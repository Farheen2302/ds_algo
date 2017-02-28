# Top Down 
def mergesort(list):
	if len(list) > 1:
		mid = len(list) // 2
		left = mergesort(list[:mid])
		right = mergesort(list[mid:])
		return _mergesort(left, right)
	else:
		return list


# Helper merge function
def _mergesort(left, right):
	i, j = 0, 0
	newarr = []
	while(len(newarr) < len(left) + len(right)):
		if left[i] < right[j]:
			newarr.append(left[i])
			i += 1
		else:
			newarr.append(right[j])
			j += 1
		if i == len(left) or j == len(right):
			newarr.extend(left[i:] or right[j:])
	return newarr


# Test cases
# Odd number of elements
assert mergesort([7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7]
# Even number of elements
assert mergesort([6,5,4,3,2,1]) == [1,2,3,4,5,6]
# Repetition of elements
assert mergesort([6,5,4,3,2,1,6]) == [1,2,3,4,5,6,6]

