from hammingDistance import hammingDistance
import math

def motifEnumeration(input, k, d):
    dnas = input.split()
    patterns = []
    kmers = []
    for i in range(0, int(math.pow(4, k))):
        cur = i;
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
        kmers.append(sb)
    for kmer in kmers:
        count = 0
        for dna in dnas:
            for i in range(0, len(dna) - k + 1):
                if hammingDistance(kmer, dna[i:i+k]) <= d:
                    count = count + 1
                    break
        if count == len(dnas):
            patterns.append(kmer)
    patterns = set(patterns)
    for p in patterns:
    	print p
    return


