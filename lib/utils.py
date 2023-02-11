import codecs
import numpy
from base64 import b64encode

    
class Convert:
    def __init__(self):
        pass

    def decode_str(self, encoded_str):
        decoded_str = codecs.decode(encoded_str, 'hex')

        decoded_str = [chr(i) for i in decoded_str]
        decoded_str = ''.join(decoded_str)

        return decoded_str

    def hex_to_b64(self, hex_str):
        hex_str_encoded = codecs.decode(hex_str, 'hex')
        b64 = codecs.encode(hex_str_encoded, 'base64')

        # [:-1] removes the tailing newline character ('\n')
        return b64.decode('ascii')[:-1]

class Xor:
    def __init__(self):
        pass
    
    def equal_len_xor(self, str1, str2):
        encoded_str1 = codecs.decode(str1, 'hex')
        encoded_str2 = codecs.decode(str2, 'hex')
        
        # format(decimal, 'x') returns the hex equivalent of 
        # decimal without 0x
        xor_str = [format(i^j, 'x') for i,j in zip(encoded_str1, encoded_str2)]

        xor_str = ''.join(xor_str)
        
        return xor_str
    
    def singlebyte_xor(self, in_str, key):
        encoded_instr = codecs.decode(in_str, 'hex')

        xor_str = [chr(i^key) for i in encoded_instr]
        #print(xor_str)
        xor_str = ''.join(xor_str)

        #print(xor_str)
        return xor_str

    def repeated_xor(self, in_str, key):
        #encoded_instr = codecs.decode(in_str, 'hex')

        # i = 0
        # while (i < len(in_str)):
        xor_str = []
        for i,j in zip(in_str,range(len(in_str))):
            j %= len(key)
            xor_str.append(ord(key[j])^ord(i))

        # convert bytes to hex
        result = bytes(xor_str).hex()

        return result

class FreqAnalysis:
    def __init__(self):
        pass

    def freq_analysis(self, in_str):
        eng_freq = {
            'E': 11.1607, 'M': 3.0129,
            'A': 8.4966, 'H': 3.0034,
            'R': 7.5809, 'G': 2.4705,
            'I': 7.5448, 'B': 2.0720,
            'O': 7.1635, 'F': 1.8121,
            'T': 6.9509, 'Y': 1.7779,
            'N': 6.6544, 'W': 1.2899,
            'S': 5.7351, 'K': 1.1016,
            'L': 5.4893, 'V': 1.0074,
            'C': 4.5388, 'X': 0.2902,
            'U': 3.6308, 'Z': 0.2722,
            'D': 3.3844, 'J': 0.1965,
            'P': 3.1671, 'Q': 0.1962
        }
        in_str = in_str.upper()

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        str_freq = dict.fromkeys(alphabet, 0)
        
        for i in in_str:
            if (i in str_freq):
                str_freq[i] += 1
        
        #len_str_freq = sum(str_freq.values())
        len_str_freq = len(in_str)
        ignored = len(in_str) - sum(str_freq.values())

        for i in str_freq:
            if(len_str_freq != 0):
                str_freq[i] = str_freq[i]/len_str_freq * 100 + ignored


        
        chi2 = 0

        # we will use a chi-squared test
        for i in str_freq:
            observed = str_freq[i]
            expected = eng_freq[i]
            chi2 += (observed - expected)**2 / expected
        
        # accumulator = 0
        # for i in str_freq:
        #     accumulator += numpy.sqrt((str_freq[i] - eng_freq[i])**2)
        
        return chi2

class Misc (Xor, FreqAnalysis):
    def __init__(self):
        #super().__init__()
        pass
    
    def find_xor_key(self, in_str):
        xor_str = []
        for key in range(0, 256):
            xor_str.append(Xor().singlebyte_xor(in_str, key))
        
        xor_str_dist = []

        for i in xor_str:
            xor_str_dist.append(FreqAnalysis().freq_analysis(i))
        
        min = xor_str_dist[0]
        index = 0
        for i in range(len(xor_str_dist)):
            if (min > xor_str_dist[i]):
                min = xor_str_dist[i]
                index = i
        
        # key = 'A'
        # if (index <= 25):
        #     key = chr(index+ord('A'))
        # else:
        #     key = chr(index+ord('a'))
        key = chr(index)
        
        return key
    