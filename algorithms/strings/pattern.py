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

text = 'abcwerfabcabc'
pattern = 'abc'
naive_match(pattern, text)
