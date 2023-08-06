# s = set()
# for _ in range(int(input())):
#     s.add(input().strip())
# print(len(s))
# print(s)

print(len(set(input().strip() for _ in range(int(input())))))
