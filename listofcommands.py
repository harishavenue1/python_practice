n, setA = int(input()), set(map(int, input().split()))
# for _ in range(int(input())):
#     k_v = input()
#     if k_v.split()[0].lower() == 'pop':
#         setA.pop()
#     elif k_v.split()[0].lower() == 'remove':
#         setA.remove(int(k_v.split()[1]))
#     elif k_v.split()[0].lower() == 'discard':
#         setA.discard(int(k_v.split()[1]))
#     else:
#         continue
# print(sum(setA))

# or
for _ in range(int(input())):
    eval('setA.{0}({1})'.format(*input().split()+['']))
print(sum(setA))

# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5
# Sample Output

# 4
