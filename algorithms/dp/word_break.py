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
	bol_arr = [False]*len(word)



print(check_word(['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice',
                  'cream', 'icecream', 'man', 'go', 'mango'], 'ilikesamsung'))
print(memo_check_word(['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice',
                       'cream', 'icecream', 'man', 'go', 'mango'], 'ilikeapple', {}))
 