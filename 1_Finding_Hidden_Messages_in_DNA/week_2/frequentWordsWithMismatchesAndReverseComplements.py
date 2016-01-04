from hammingDistance import hammingDistance
import math

def frequentWordsWithMismatchesAndReverseComplements(text, k, d):
    count = dict()
    for i in range(0, int(math.pow(4, k))):
        cur = i
        sb = ''
        for j in range(0, k):
            if cur % 4 == 0:
                sb = sb + 'A'
            elif cur % 3 == 1:
                sb = sb + 'C'
            elif cur % 3 == 2:
                sb = sb + 'G'
            else:
                sb = sb + 'T'
            cur = cur / 4
        count[sb] = 0
    for key,value in count.items():
        for i in range(0, len(text) - k + 1):
            if hammingDistance(key,text[i:i+k]) <= d:
                count[key] = count[key] + 1
    max = 0
    result = dict()
    for key,value in count.items():
    	reverse = reverseComplement(key)
        result[key] = count[key] + count[reverse]
        if result[key] > max:
        	max = result[key]
    for key,value in result.items():
        if value == max:
        	print key,
    return

def reverseComplement(text):
    text = text.replace(' ','')
    sb = ''
    for i in range(1, len(text) + 1):
        if cmp(text[len(text) - i], 'A') == 0: 
            sb = sb + 'T'
        elif cmp(text[len(text) - i], 'T') == 0:
            sb = sb + 'A'
        elif cmp(text[len(text) - i], 'C') == 0:
            sb = sb + 'G'
        else:
            sb = sb + 'C'
    return sb