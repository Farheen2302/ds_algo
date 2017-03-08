def quicksort(arr, start, end):
    if start < end:
        pivot = _quicksort(arr, start, end)
        left = quicksort(arr, 0, pivot - 1)
        right = quicksort(arr, pivot + 1, end)
    return arr


def _quicksort(arr, start, end):
    pivot = start
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] < arr[pivot]:
            left += 1
        while right >= left and arr[right] > arr[pivot]:
            right -= 1
        if left >= right:
            done = True
        else:
            """ Making use of python's swapping technique
            http://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python """
            arr[left], arr[right] = arr[right], arr[left]
            #swap(arr, left, right)
    arr[pivot], arr[right] = arr[right], arr[pivot]
    #swap(arr, pivot, right)
    return right


def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp


# Test Cases
arr = [8, 7, 6, 5, 4, 3, 2, 1]
arr1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
assert sorted(arr1) == quicksort(arr1, 0, len(arr1) - 1)
assert sorted(arr) == quicksort(arr, 0, len(arr)-1)
