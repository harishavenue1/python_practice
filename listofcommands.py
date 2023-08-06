n, setA = int(input()), set(map(int, input().split()))
for _ in range(int(input())):
    k, *v = input().split()
    if k == 'pop':
        setA.pop()
    elif k.lower() == 'remove':
        setA.remove(int(str(*v)))
    elif k.lower() == 'discard':
        setA.discard(int(str(*v)))
    else:
        continue
print(sum(setA))

# or
for _ in range(int(input())):
    eval('setA.{0}({1})'.format(*input().split()+['']))
print(sum(setA))
