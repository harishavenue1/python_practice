import re
inp: str = '1000,000,000.000'
pattern = r'[.,]'

# here r is used to make all chars inside [] as normal char
# else . char will be treated as special char
# [] is expected format
# used to group all chars which needs to be split based on

# if only .
pattern = r'[.]'

# if only ,
pattern = r'[,]'
print('\n'.join(re.split(pattern, inp)))