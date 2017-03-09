""" When we perform  left rotations, the array undergoes the following sequence of changes:

Thus, we print the array's final state as a single line of space-separated values, which is 5 1 2 3 4. """

n, d = map(int, input().split())
arr = [int(x) for x in input().split()]

# Easy Solution (O(d*n))
def left_rotate(arr, d, n):
    for i in range(d):
        _left_rotate(arr, n)
    return arr


def _left_rotate(arr, n):
    temp, i = arr[0], 0
    while i < n - 1:
        arr[i] = arr[i + 1]
        i += 1
    arr[i] = temp
    return arr

left_rotate(arr, d, n)
[print(i, end=" ") for i in arr]


# Better solution
for i in range(n):
	m = d + i
	if m > n-1:
		m %= n
	print(arr[m], end=' ')