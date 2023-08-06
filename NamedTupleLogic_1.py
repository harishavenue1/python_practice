from collections import namedtuple

n = int(input())
score = namedtuple('Score', input().split())
avg = sum([int(score(*input().split()).MARKS) for i in range(n)]) / n
print(f"{avg:.2f}")
