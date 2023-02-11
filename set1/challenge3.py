import sys
sys.path.append('../')

from lib.utils import Misc, Xor

in_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

key = Misc().find_xor_key(in_str)
msg = Xor().singlebyte_xor(in_str, ord(key))

print("The key is: ", key)
print("The message: ", msg)