def patternCount(pattern, text):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        #print pattern
        #print text[i : i + len(pattern)]
        if cmp(text[i : i + len(pattern)], pattern) == 0:
            count = count + 1
    return count

