import sys
import math
from hammingDistance import hammingDistance

def medianString(input, k):
    dnas = input.split()
    distance = sys.maxint
    kmers = []
    median = ''
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
        kmers.append(sb)
    for kmer in kmers:
        distanceSum = 0
        for dna in dnas:
            d = sys.maxint 
            for i in range(0, len(dna) - k + 1):
                if hammingDistance(kmer, dna[i:i+k]) < d:
                    d = hammingDistance(kmer, dna[i:i+k])
            distanceSum = distanceSum + d
        if distanceSum < distance:
            distance = distanceSum
            median = kmer
    print distance
    print median
    return  
