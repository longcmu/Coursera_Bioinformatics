def minimumSkew(path):
    fo = open(path)
    genome = fo.read()
    genome = genome.replace(' ','')
    fo.close()
    list = [0]
    min = 0
    for i in range(0, len(genome)):
        if cmp(genome[i], 'C') == 0:
            list.append(list[-1] - 1)
        elif cmp(genome[i], 'G') == 0:
            list.append(list[-1] + 1)
        else:
            list.append(list[-1])
        if list[-1] < min:
            min = list[-1]
    fileHandle = open('result.txt', 'w')
    for j in range(0, len(list)):
        if list[j] == min:
            fileHandle.write(str(j) + ' ')
    fileHandle.close()
    return
