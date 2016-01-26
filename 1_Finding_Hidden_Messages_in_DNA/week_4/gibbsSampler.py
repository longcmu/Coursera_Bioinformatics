import random, sys

def gibbsSampler(input, k, t, n):
    random.seed()
    minScore = sys.maxint
    bestMotifs = []
    dnas = input.split()
    for i in range(0, 100):
        print i
        curMotifs = gibbsSampler_(dnas, k, t, n)
        curScore = getScore(curMotifs)
        if curScore < minScore:
            minScore = curScore
            bestMotifs = curMotifs
    for bestMotif in bestMotifs:
        print bestMotif
    print getScore(bestMotifs)

def gibbsSampler_(dnas, k, t, n):
    motifs = []
    bestMotifs = []
    for i in range(0, t):
        rand = random.randint(0, len(dnas[0]) - k)
        motifs.append(dnas[i][rand:rand+k])
    bestMotifs = motifs
    for j in range(0, n):
        i = random.randint(0, t - 1)
        profile = generateProfile(motifs[:i] + motifs[(i + 1):])
        motifs[i] = generateKmerRandomly(dnas[i], profile, k)
        if getScore(motifs) < getScore(bestMotifs):
            bestMotifs = motifs
    return bestMotifs

def generateKmerRandomly(dna, profile, k):
    kmers = []
    probs = []
    for i in range(0, len(dna) - k + 1):
        kmer = dna[i:i+k]
        prob = 1.0
        for j in range(0, len(kmer)):
            cur = kmer[j]
            if cur == 'A':
                prob = prob * profile[0][j]
            elif cur == 'C':
                prob = prob * profile[1][j]
            elif cur == 'G':
                prob = prob * profile[2][j]
            else:
                prob = prob * profile[3][j]
        kmers.append(kmer)
        probs.append(prob)
    probSum = 0
    for prob in probs:
        probSum = probSum + prob
    for i in range(0, len(probs)):
        probs[i] = probs[i] / probSum * 100
    rand = random.randint(0, 99)
    for i in range(0, len(probs)):
        rand = rand - probs[i]
        if rand < 0:
            return kmers[i]

def generateKmerRandomly_(dna, profile, k):
    kmers = []
    probs = []
    for i in range(0, len(dna) - k + 1):
        kmer = dna[i:i+k]
        prob = 1.0
        for j in range(0, len(kmer)):
            cur = kmer[j]
            if cur == 'A':
                prob = prob * profile[0][j]
            elif cur == 'C':
                prob = prob * profile[1][j]
            elif cur == 'G':
                prob = prob * profile[2][j]
            else:
                prob = prob * profile[3][j]
        kmers.append(kmer)
        probs.append(prob)
    probSum = 0
    for prob in probs:
        probSum = probSum + prob
    for i in range(0, len(probs)):
        probs[i] = probs[i] / probSum * 100
    rand = random.randint(0, 99)
    for i in range(0, len(probs)):
        rand = rand - probs[i]
        if rand < 0:
            return kmers[i]

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