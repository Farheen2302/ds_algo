# naive approach
def naive_match(pattern, text):
    result = []
    P = len(pattern)
    T = len(text)
    for i in range(0, T - P + 1):
        for j in range(P):
            if pattern[j] != text[i + j]:
                break
        if j == P - 1:
            result.append(i)
    return (result)

# Refer : https://www.coursera.org/learn/algorithms-on-strings/lecture/5lDsK/computing-prefix-function
# KMP method takes linear time O(P+T), but the prefix function should be
# computed first.


def compute_prefix(text):
    result = [0]
    border = 0
    for i in range(1, len(text)):
        while border > 0 and text[i] != text[border]:
            border = result[border - 1]
        if text[i] == text[border]:
            border += 1
        else:
            border = 0
        result.append(border)
    return result


def kmp_match(pattern, text):
    result = []
    s = pattern + '#' + text
    P = len(pattern)
    T = len(text)
    prefix = compute_prefix(s)
    for i in range(P - 1, len(s)):
        if prefix[i] == P:
            result.append(i - 2 * P)
    return (result)

text = 'abcwerfabcabc'
pattern = 'abc'
assert kmp_match(pattern, text) == [0, 7, 10]
assert kmp_match('aaba', 'aabaacaadaabaaba') == [0, 9, 12]
assert naive_match(pattern, text) == [0, 7, 10]
