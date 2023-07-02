# def char_range(n0, n50):
#         for c in range(ord(n0), ord(n50) + 1):
#             yield chr(c)
# for c in char_range('a', 'z'):
#     print(c)

# import itertools
#
# input = '[AAA] Grim'
# n = len(input.split(' ')[0]) - 2
# s = input[n+2:]
# a = [''.join(x)+s for x in itertools.product(string.ascii_lowercase, repeat=n)]

import re
import string
import itertools

user_in = input("Enter string: ")
p_len = user_in.index(']') - user_in.index('[')
text = user_in[user_in.index(']')+1:]
print('\n'.join([ ''.join(p) + text for p in itertools.combinations_with_replacement(string.ascii_lowercase,r=p_len-1)]))