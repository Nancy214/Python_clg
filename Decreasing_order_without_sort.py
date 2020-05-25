# Given a string, sort it in decresing order based on the frequency of characters
from collections import *
s = input('Enter string: ')
#str_rev = sorted(s, reverse = True)
for c, t in Counter(s).most_common():
    print(''.join(c*t),end='')
