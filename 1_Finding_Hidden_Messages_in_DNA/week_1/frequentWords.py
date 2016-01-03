from patternCount import patternCount

def frequentWords(text, length):
    dict = {}
    maxLen = 1
    for i in range(0, len(text) - length + 1):
        pattern = text[i : i + length]
        if not pattern in dict:
            curLen = patternCount(pattern, text)
            if curLen >= maxLen:
                maxLen = curLen
                dict[pattern] = curLen
    print dict

