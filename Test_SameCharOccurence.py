# Enter your code here. Read input from STDIN. Print output to STDOUT

st = input()

temp = st[0] if st[0].isalnum() else ''

for s in st[1:]:
    if s.isalnum():
        if s == temp:
            temp += s
        else:
            temp = s
        if len(temp) > 1:
            break

print(temp[0] if len(temp) > 1 else '-1')

