n, m = map(int, input().split())

list_A = []

list_B = []

for i in range(n):
    list_A.append(input().strip())

for j in range(m):
    list_B.append(input().strip())

for i in list_B:
    final1 = []
    for j in range(len(list_A)):
        if i == list_A[j]:
            b = j + 1
            final1.append(b)

    if len(final1) > 0:
        print(' '.join(map(str, final1)))
    else:
        print('-1')
