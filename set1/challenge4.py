import sys
sys.path.append('../')

from lib.utils import FreqAnalysis, Misc, Convert, Xor

filename = '4.txt'

file = open(filename)
lines = file.read().splitlines()


strings = dict()

for line in lines:
    key = Misc().find_xor_key(line)
    strings[line] = FreqAnalysis().freq_analysis (
                                        Xor().singlebyte_xor(line, ord(key))
                                    )

# plaintext = dict()
# for i in strings:
#     key = Misc().find_xor_key(line)
#     plaintext[Xor().singlebyte_xor(line, ord(key))]


dict_key = min(strings, key=strings.get)

key = Misc().find_xor_key(dict_key)
print("Likely plaintext is: ", Xor().singlebyte_xor(dict_key, ord(key)))
print("With HEX value of: ", dict_key)
print(" and key: ", ord(key))

#print(sorted(strings, key=strings.get))

# strings = dict(sorted(strings.items(), key=lambda item: item[1]))
# j = 0
# for i in strings:
#     if (j < 5):
#         print(i, "---", strings[i])

#     j+= 1

'''
strings = []
for line in lines:
    key = Misc().find_xor_key(line)
    strings.append(Xor().singlebyte_xor(line, ord(key)))

strings.reverse()

freq = []
for string in strings:
    freq.append(FreqAnalysis().freq_analysis(string))

freq.reverse()

smallest = freq[0]
tmp = 0

# for i in freq:
#     print(i)

for i in range(len(freq)):
    if (smallest > freq[i]):
        smallest = freq[i]
        tmp = i

print(strings[tmp])
'''