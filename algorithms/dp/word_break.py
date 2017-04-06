# Refer :
# http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/


def check_word(dictionary, word):
	if len(word) == 0:
		return True
	for i in range(len(word)):
		prefix = word[:i + 1]
		suffix = word[i + 1:len(word)]
		if prefix in dictionary and check_word(dictionary, suffix):
			return True
	return False

# Memoization approach


def memo_check_word(dictionary, word, result):
	if len(word) == 0:
		return True
	if word in result:
		return result[word]
	for i in range(len(word)):
		prefix = word[:i + 1]
		suffix = word[i + 1:len(word)]
		if prefix in dictionary and memo_check_word(dictionary, suffix, result):
			result[word] = True
			return True
	result[word] = False
	return False


def dp_check_word(dictionary, word):
	bol_arr = [False] * len(word)
	for i in range(len(word)):
		if bol_arr[i] is False and word[:i + 1] in dictionary:
			bol_arr[i] = True
		if bol_arr[i]:
			if i == len(word) - 1:
				return True
			for j in range(i + 1, len(word)):
				if bol_arr[j] is False and word[i + 1:j + 1] in dictionary:
					bol_arr[j] = True
				if j == len(word) - 1 and bol_arr[j] is True:
					print(bol_arr)
					return True
	print(bol_arr)
	return False


print(check_word(['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice',
				  'cream', 'icecream', 'man', 'go', 'mango'], 'ilikesamsung'))
print(memo_check_word(['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice',
					   'cream', 'icecream', 'man', 'go', 'mango'], 'ilikeapple', {}))
print(dp_check_word(['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice',
					 'cream', 'icecream', 'man', 'go', 'mango'], 'ilikesamsung'))
