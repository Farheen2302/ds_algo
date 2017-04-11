def rec_sum_sq(sqsum, arr, index, total, sol, count):
	print("SQ Sum: " + str(sqsum) + " arr: " + str(arr) + " index: " +
		  str(index) + " total: " + str(total) + " count : " + str(count))
	if sqsum == total:
		sol.append(count)
		return count
	if index == len(arr) - 1:
		return 0
	for i in arr:
		sqsum += i * i
		count += 1
		if sqsum > total:
			sqsum -= i * i
			rec_sum_sq(sqsum, arr, index + 1, total, sol, count - 1)
		else:
			rec_sum_sq(sqsum, arr, index, total, sol, count)
	print(sol)

rec_sum_sq(0, [1, 2, 3], 0, 12, [], 0)
