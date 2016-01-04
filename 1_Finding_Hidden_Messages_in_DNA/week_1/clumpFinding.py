import math

def clumpFinding(genome, k, l, t):
    genome = genome.replace(' ','')
    fileHandle = open('result.txt', 'w')
    count = dict()
    s = set()
    for i in range(0, len(genome) - l + 1):
    	cur = genome[i:i+l]
    	for r in range(0, len(cur)):
    		count[cur[r:r+k]] = 0
        for j in range(0, l - k + 1):
        	kmer = genome[i+j : i+j+k]
        	count[kmer] = count[kmer] + 1
        for d,x in count.items():
            if x >= t and not d in s:
                fileHandle.write(str(d) + ' ')
                s.add(d)
    fileHandle.close()
    return