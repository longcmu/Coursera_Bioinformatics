from hammingDistance import hammingDistance
import math

def frequentWordsWithMismatches(text, k, d):
    count = dict()
    max = 0
    for i in range(0, int(math.pow(4, k))):
        cur = i
        sb = ''
        for j in range(0, k):
            if cur % 4 == 0:
                sb = sb + 'A'
            elif cur % 4 == 1:
                sb = sb + 'C'
            elif cur % 4 == 2:
                sb = sb + 'G'
            else:
                sb = sb + 'T'
            cur = cur / 4
        count[sb] = 0
    for key,value in count.items():
        for i in range(0, len(text) - k + 1):
            if hammingDistance(key,text[i:i+k]) <= d:
                count[key] = count[key] + 1
                if count[key] > max:
                    max = count[key]
    for key,value in count.items():
        if value == max:
            print key,
    return
