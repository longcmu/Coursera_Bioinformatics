from patternCount import patternCount

def frequentWords(text, length):
    text = text.replace(' ','')
    stat = {}
    maxLen = 1
    for i in range(0, len(text) - length + 1):
        pattern = text[i : i + length]
        if not pattern in stat:
            curLen = patternCount(pattern, text)
            if curLen >= maxLen:
                maxLen = curLen
                stat[pattern] = curLen
    print stat

