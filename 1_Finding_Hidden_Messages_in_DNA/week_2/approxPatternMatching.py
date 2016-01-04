from hammingDistance import hammingDistance

def approxPatternMatching(pattern, text, k):
    pattern = pattern.replace(' ','')
    text = text.replace(' ','')
    for i in range(0, len(text) - len(pattern) + 1):
        if hammingDistance(pattern, text[i:i+len(pattern)]) <= k:
            print i,
    return
