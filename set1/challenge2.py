import sys
sys.path.append('../')

from lib.utils import Xor

in_str1 = '1c0111001f010100061a024b53535009181c'
in_str2 = '686974207468652062756c6c277320657965'

expected_output = "746865206b696420646f6e277420706c6179"

result = Xor().equal_len_xor(in_str1, in_str2)

assert(result == expected_output)

print(result)