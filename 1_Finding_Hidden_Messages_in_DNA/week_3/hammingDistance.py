def hammingDistance(s1, s2):
    s1 = s1.replace(' ','')
    s2 = s2.replace(' ','')
    count = 0
    for i in range(0, len(s1)):
        if cmp(s1[i], s2[i]) != 0:
            count = count + 1
    return count
