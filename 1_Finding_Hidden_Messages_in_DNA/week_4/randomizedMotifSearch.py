import random, sys

def randomizedMotifSearch(input, k, t):
    random.seed()
    minScore = sys.maxint
    motifs = []
    for i in range(0, 1000):
        curMotifs = randomizedMotifSearch_(input, k, t)
        curScore = getScore(curMotifs)
        if curScore < minScore:
            minScore = curScore
            motifs = curMotifs
    for motif in motifs:
        print motif
    print minScore
    return

def randomizedMotifSearch_(input, k, t):
    dnas = input.split()
    motifs = []
    bestMotifs = []
    for i in range(0, t):
        rand = random.randint(0, len(dnas[0]) - k)
        motifs.append(dnas[i][rand:rand+k])
    bestMotifs = motifs
    while True:
        profile = generateProfile(motifs)
        motifs = []
        for j in range(0, len(dnas)):
            motifs.append(profilemostProbableKmer(dnas[j], k, profile))
        if getScore(motifs) < getScore(bestMotifs):
            bestMotifs = motifs
        else:
            return bestMotifs

def profilemostProbableKmer(dna, k, matrix):
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
    return result

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