import re
s = 'aaadaa'
k = 'aa'

#1
m = re.search(k, s)
pattern = re.compile(k)
if not m:
    print((-1,-1))
while m:
    print("({0}, {1})".format(m.start(), m.end()-1))
    m = pattern.search(s, m.start()+1)

print("------------------")

# 2
for i,_ in enumerate(s):
    if re.match(k, s[i:]):
        print((i, i+len(k)-1))

if re.search(k,s) == None:
    print((-1, -1))

print("------------------")
pattern = r'(?='+k+')'
# print index of char repeated
if k in s:
    print(*[(i.start(), i.start()+len(k)-1) for i in re.finditer(pattern, s)], sep='\n')
else:
    print((-1,-1))