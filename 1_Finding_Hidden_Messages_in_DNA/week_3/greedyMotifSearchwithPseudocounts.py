def greedyMotifSearchwithPseudocounts(k, t, input):
    dnas = input.split(',')
    bestMotifs = []
    for i in range(0, len(dnas)):
        bestMotifs.append(dnas[i][0:0+k])
    for i in range(0, len(dnas[0]) - k + 1):
        motifs = []
        motifs.append(dnas[0][i:i+k])
        for j in range(1, t):
            profile = generateProfile(motifs)
            kmer = profilemostProbableKmer(dnas[j], k, profile)
            motifs.append(kmer)
        if getScore(motifs) < getScore(bestMotifs):
            bestMotifs = motifs
    print bestMotifs
    return

def getScore(motifs):
    score = 0
    for i in range(0, len(motifs[0])):
        stat = {'A':0, 'C':0, 'G':0, 'T':0}
        for motif in motifs:
            stat[motif[i]] = stat[motif[i]] + 1
        maxVal = 0
        for k, v in stat.items():
            if v > maxVal:
                maxVal = v
        score = score + len(motifs) - maxVal 
    return score

def profilemostProbableKmer(dna, k, matrix):

    maxProb = 0
    result = dna[0:0+k]
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
    return result

def generateProfile(dnas):
    matrix = []
    for i in range(0, 4):
        row = []
        for j in range(0, len(dnas[0])):
            row.append(1)
        matrix.append(row)
    for i in range(0, len(dnas[0])):
        for j in range(0, len(dnas)):
            if dnas[j][i] == 'A':
                matrix[0][i] = matrix[0][i] + 1
            elif dnas[j][i] == 'C':
                matrix[1][i] = matrix[1][i] + 1
            elif dnas[j][i] == 'G':
                matrix[2][i] = matrix[2][i] + 1
            else:
                matrix[3][i] = matrix[3][i] + 1
    for i in range(0, len(dnas[0])):
        colSum = matrix[0][i] + matrix[1][i] + matrix[2][i] + matrix[3][i]
        for j in range(0, 4):
            matrix[j][i] = matrix[j][i] * 1.0 / colSum
    return matrix
