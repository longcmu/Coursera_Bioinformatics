def patternMatching(pattern, text):
    pattern = pattern.replace(' ','')
    text = text.replace(' ','')
    for i in range(0, len(text) - len(pattern) + 1):
        if cmp(text[i:i+len(pattern)], pattern) == 0:
            print i,
    return
