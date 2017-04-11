import math


def ugly(n):
    arr = [1]
    i = 2
    c = 0
    while c <= n:
        pow_2 = greatest_pow(i, 2)
        pow_3 = greatest_pow(pow_2, 3)
        if n / pow_3 == 1:
            arr.append(i)
            c += 1
        i += 1
    print(arr)


def greatest_pow(num, div):
    p = 1
    while num % math.pow(div, p) == 0:
        p += 1
    return int(math.pow(div, p - 1))

print(ugly(11))
