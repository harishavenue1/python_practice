import re
inp = '01234567891011121314151617181922' #111
pattern = r'([0-9a-zA-z])\1' #1 says match same text at most
pattern = r'(\w(?!_))\1' # here \w is for alphanumeric, and ? means 0/1 occurrence of not _ key
m = re.search(pattern, inp)

# match() -------- > >> Determine if the RE matches at the beginning of the string.
# search() ---------> >> Scan through a string, looking for any location where this RE matches.
# findall() ---- ----->>> Find all substrings where the RE matches, and returns them as a list.
# finditer()----->>> Find all substrings where the RE matches, and returns them as an iterator.

if m:
    print(m.start())
    print(m.end())
    print(m.span())
    print(m.group())
    print(*m.group())
    print(m.groups())
else:
    print(-1)

s="abc def aaa bbb ccc def hhh"
m = [(x.start(),x.end()) for x in re.finditer(r'(\w)\1', s)]
print(m)