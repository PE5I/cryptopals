import sys
sys.path.append('../')

from lib.utils import Convert


hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expected_output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

b64_str = Convert().hex_to_b64(hex_str)

assert(b64_str == expected_output)
print(b64_str)