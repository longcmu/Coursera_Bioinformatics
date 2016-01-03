import sys

def reverseComplement(text):
    fileHandle = open('result.txt', 'w')
    for i in range(1, len(text) + 1):
        if cmp(text[len(text) - i], 'A') == 0: 
            fileHandle.write('T')
        elif cmp(text[len(text) - i], 'T') == 0:
            fileHandle.write('A')
        elif cmp(text[len(text) - i], 'C') == 0:
            fileHandle.write('G')
        else:
            fileHandle.write('C')
    fileHandle.close()
    return
