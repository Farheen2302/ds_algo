# Recursive apprach. This will give way to memoization in DP.


def knapsack(val, wt, currWt, index):
    if currWt == 0 or index == len(wt):
        return 0
    else:
        if wt[index] > currWt:
            return knapsack(val, wt, currWt, index + 1)
        else:
            return max(val[index] + knapsack(val, wt, currWt - wt[index], index + 1), knapsack(val, wt, currWt, index + 1))

# DP with memoization


def memo_knapsack(val, wt, currWt, index, result={0: 0}):
    if currWt in result:
        return result[currWt]
    if index == len(wt):
        return 0
    else:
        if wt[index] > currWt:
            result[currWt] = memo_knapsack(val, wt, currWt, index + 1)
            return result[currWt]
        else:
            result[currWt] = max(val[index] + memo_knapsack(val, wt, currWt -
                                                            wt[index], index + 1), memo_knapsack(val, wt, currWt, index + 1))
            return result[currWt]

# TO DO
# def bu_knapsack(val, wt, currWt):


val = [60, 100, 120]
wt = [10, 20, 30]
currWt = 50
print(memo_knapsack(val, wt, currWt, 0))
