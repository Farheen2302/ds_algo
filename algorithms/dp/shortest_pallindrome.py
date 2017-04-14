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


word = 'ananab'
com_word = word + '#' + word[::-1]
lcs = compute_prefix(com_word)
assert (com_word[len(word) + 1:(len(com_word) - lcs[-1])]) == 'b'
