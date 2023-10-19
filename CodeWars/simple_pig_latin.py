def pig_it(text):
    words = text.split()
    for word in range(len(words)):
        words[word] = words[word][1:] + words[word][0] + 'ay'
    return ' '.join(words)
print(pig_it('Как все же хорошо'))