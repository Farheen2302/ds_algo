def shellsort(arr):
    shifts = len(arr) // 2
    while shifts > 0:
        for i in range(shifts):
            _shellsort(arr, i, shifts)
        shifts = shifts // 2
    return arr


def _shellsort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        pos = i
        current = arr[i]
        while pos > 0 and arr[pos - 1] > current:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = current
    return arr

arr = [7, 6, 5, 43, 7, 1, 76, -33]
assert shellsort(arr) == [-33, 1, 5, 6, 7, 7, 43, 76]
