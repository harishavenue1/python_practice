from collections import namedtuple
N, student = int(input()), namedtuple('student', input().split())
avg = sum([int(student(*input().split()).MARKS) for i in range(N)])/N
print(f"{avg:.2f}")
