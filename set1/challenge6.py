import numpy as np
import sys
sys.path.append('../')

from lib.utils import FreqAnalysis, Misc, Convert, Xor

from base64 import b64decode
import codecs

# Compute the hamming bit distance between two strings
def hamming(str1, str2):
    if (len(str1) != len(str2)):
        return 1
    
    encoded_str1 = bytearray(str1.encode())
    encoded_str2 = bytearray(str2.encode())
    
    distance = 0
    for i,j in zip(encoded_str1, encoded_str2):
        distance += bin(int(i)^int(j)).count('1')
    
    return distance



str1 = "this is a test"
str2 = "wokka wokka!!!"

assert(hamming(str1, str2) == 37)

filename = '6.txt'

ifile = open(filename)
b64text = ifile.read()
ciphertext = b64decode(b64text)

normal_avg = {}
for keysize in range(2,41):
    
    distances = []
    chunks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]

    i = 1
    while (i < len(chunks)):
        try:
            dist = hamming(chunks[i-1].hex(), chunks[i].hex())
            normal = dist / keysize
            distances.append(normal)
            i += 2
        except Exception as e:
            pass
    #print(len(chunks))
    #print(distances)
    if (len(distances) != 0):
        list_sum = sum(distances)/len(distances)
        normal_avg[str(keysize)] = list_sum

sorted_avg = sorted(normal_avg.items(), key=lambda x:x[1])

# Likely key is the first entry in sorted_avg, but we will proceed with 2
# or 3 keys in sorted_avg

# probably keysize
pkeysize = int(sorted_avg[0][0])
# print(pkeysize)

# Break the ciphertext into blocks of keysize length
chunks = []


for i in range(0, len(ciphertext), pkeysize):
    chunks.append(ciphertext[i:i+pkeysize])


# chunks = np.array(chunks)
# chunks_T = chunks.transpose()

# print(chunks)
# print(chunks)
# def transpose(ilist):
#     tmp = []
#     ilist_T = []
#     for i in range(len(ilist[0])):
#         # for j in range(len(ilist)-1):
#         #     tmp.append(ilist[j][i])
#         # ilist_T.append(tmp)
#         # tmp = []
#         ilist_T.append([ilist[j][i] for j in range(len(ilist))])
    
    
#     return ilist_T

# chunks_T = transpose(chunks)

# print(chunks_T)

# a = ["abc", "def", "ghi", "fgp"]
# print(transpose(a))