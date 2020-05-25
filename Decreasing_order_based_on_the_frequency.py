# Given a string, sort it in decresing order based on the frequency of characters
from collections import Counter
s = input('Enter string: ')
str_dict = dict(Counter(s))
l = []
for k in sorted(str_dict,key = str_dict.get, reverse = True):
    for i in range(str_dict[k]):
        l.append(k)
print("".join(l))

