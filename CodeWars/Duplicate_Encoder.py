def duplicate_encode(word):
    word = word.lower()
    count = {}
    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = ''
    for char in word:
        if count[char] > 1:
            result += ')'
        else:
            result += '('
    return result