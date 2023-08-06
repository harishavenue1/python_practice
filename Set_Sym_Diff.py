# set1 = set(map(int, input().split()) for _ in range(int(input())))
# set2 = set(map(int, input().split()) for _ in range(int(input())))

s1_len, set1 = int(input()), set(map(int, input().split()))
s2_len, set2 = int(input()), set(map(int, input().split()))
d1 = sorted(set1.difference(set2).union(set2.difference(set1)))
print("\n".join(map(str, d1)))
