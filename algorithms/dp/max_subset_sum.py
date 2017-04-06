import sys
# Note: The subarray should be contiguous

# The easiest (read,  most inefficient) implementation so far.
# Does not work with all negative numbers


def max_sum(arr):
    max_so_far = -sys.maxsize - 1
    curr_max = 0

    for i in arr:
        curr_max = curr_max + i
        if curr_max < 0:
            curr_max = 0
        if curr_max > max_so_far:
            max_so_far = curr_max
    return max_so_far


def dp_max_sum(arr):
    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(curr_max, max_so_far)
    return max_so_far


print(max_sum([-2, -3, 4, -1, -2, 1, 5, -3]))
print(dp_max_sum([-2, -3, -4, -1, -2, -1, -5, -3]))

