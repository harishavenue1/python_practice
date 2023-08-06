vow = '[aeiou]'
cons = '[bcdfghjklmnpqrstvwxyz]'

import re
pattern = r'(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})(?=[bcdfghjklmnpqrstvwxyz])'
# pattern = r'(?<='+cons+')('+vow+'{2,})(?='+cons+')'
# ?<= -> resembles constants before ?<=
# (vow{2,}) -> search vow repeated 2 in seq
# ?= -> resembles constants after ?=
inp = 'haariishkumarp'
a = re.findall(pattern, inp)
a = [it.group() for it in re.finditer(pattern, inp)] # gives iter object, same results
print(a)