from hammingDistance import hammingDistance

def approxPatternCount(pattern, text, d):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if hammingDistance(pattern, text[i:i+len(pattern)]) <= d:
            count = count + 1
    print count
    return
