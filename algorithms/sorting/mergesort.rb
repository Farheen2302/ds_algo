require 'test/unit'
extend Test::Unit::Assertions

def mergesort(list)
	if list.length < 2
		return list
	else
		mid = (list.length/2).to_i
		left = mergesort(list.slice(0, mid))
		right = mergesort(list.slice(mid, list.length))
		return _mergesort(left, right)
	end
end

def _mergesort(left, right)
	newarr = []
	i = j = 0
	while(newarr.length < left.length + right.length)
		if left[i] < right[j]
			newarr << left[i]
			i += 1
		else
			newarr << right[j]
			j += 1
		end
		if i == left.length
			right.slice(j, right.length).each {|x| newarr << x}
		elsif j == right.length
			left.slice(i, left.length).each {|x| newarr << x}
		end
	end
	return newarr
end

# Test cases
# Odd number of elements
assert(mergesort([7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7], "Sorry, it did not pass through")
# Even number of elements
assert(mergesort([6,5,4,3,2,1]) == [1,2,3,4,5,6], "Sorry, it did not pass through")
# Repetition of elements
assert(mergesort([6,5,4,3,2,1,6]) == [1,2,3,4,5,6,6], "Sorry, it did not pass through")
