import re
pattern = '^[-+]?[0-9]*\.[0-9]*$'
# '^' cap symbol is used to check for start '&' for end of pattern
# '?' symbol to check 0 or 1 occurrence of left pattern provided, here its -/+, 'if --10.9 then no match'
# '*' symbol to check 0 or more occurrence of left pattern provided
# '\.' symbol to check decimal dot occurrence

# can be using r as well, both gives same output

pattern = r'[-+]?[0-9]*[\.][0-9]*'

inp = '-10.9' #'-10.0'
m = re.match(pattern, inp)  # o/p is a match object
if m:
    print(m.start())
    print(m.end())
    print(m.span())
    print(m.group())
    print(*m.group())
    print(m.groups())

print('yes its a match') if m else print(-1)


