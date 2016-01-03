def patternMatching(path, pattern):
    pattern = pattern.replace(' ','')
    fo = open(path)
    text = fo.read()
    text = text.replace(' ','')
    fo.close()
    fileHandle = open('result.txt', 'w')
    for i in range(0, len(text) - len(pattern) + 1):
        if cmp(text[i:i+len(pattern)], pattern) == 0:
            fileHandle.write(str(i) + ' ')
    fileHandle.close()
    return
