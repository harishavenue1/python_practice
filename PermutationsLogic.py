from itertools import permutations

s, k = input().split()
# for i in sorted(list(permutations(s, int(k)))):
#     print(''.join(i))

print(*[''.join(i) for i in permutations(sorted(s), int(k))], sep='\n')

