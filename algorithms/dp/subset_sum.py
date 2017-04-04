def rec_sub_sum(arr, sol, index, total, currentSum):
    if currentSum == total:
        for i in range(len(sol)):
            if sol[i] == 1:
                print(arr[i], end=' ')
        return True
    elif index == len(arr):
        return
    else:
        currentSum += arr[index]
        sol[index] = 1
        rec_sub_sum(arr, sol, index + 1, total, currentSum)
        currentSum -= arr[index]
        sol[index] = 0
        rec_sub_sum(arr, sol, index + 1, total, currentSum)


def dp_sub_sum(arr, total):
    sol = [[-1 for _ in range(total + 1)] for _ in range(len(arr) + 1)]
    for i in range(len(arr)+1):
    	sol[i][0] = True
    for i in range(1, total+1):
    	sol[0][i] = False
    for i in range(1, len(arr)+1):
    	for j in range(1, total+1):
    		sol[i][j] = sol[i-1][j]
    		if arr[i-1] <= total and sol[i][j] is False:
    			sol[i][j] = sol[i][j] or sol[i-1][j-arr[i-1]]
    return (sol[len(arr)][total])

rec_sub_sum([3, 2, 7, 1], 4 * [0], 0, 6, 0)
assert dp_sub_sum([3, 2, 7, 1], 6) == True
