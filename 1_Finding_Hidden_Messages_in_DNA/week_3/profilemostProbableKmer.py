def profilemostProbableKmer(dna, k, prob):
    matrix = getMatrixProfile(prob)
    maxProb = 0
    result = ''
    for i in range(0, len(dna) - k + 1):
        kmer = dna[i:i+k]
        curProb = 1
        for j in range(0, k):
            if kmer[j] == 'A':
                curProb = curProb * float(matrix[0][j])
            elif kmer[j] == 'C':
                curProb = curProb * float(matrix[1][j])
            elif kmer[j] == 'G':
                curProb = curProb * float(matrix[2][j])
            else:        
                curProb = curProb * float(matrix[3][j])
        if curProb > maxProb:
            maxProb = curProb
            result = kmer
    print result
    return

def getMatrixProfile(prob):
    probs = prob.split(',')
    matrix = []
    for i in range(0, 4):
        matrix.append(probs[i].split())
    return matrix
