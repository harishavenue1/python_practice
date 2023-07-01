size_a, size_b = map(int, input().split())
list_a = [input().strip() for _ in range(int(size_a))]
list_b = [input().strip() for _ in range(int(size_b))]

for c1 in list_b:
    final_list = []
    for idx in range(len(list_a)):
        if c1 == list_a[idx]:
            final_list.append(idx + 1)
    if len(final_list) == 0:
        print(-1)
    else:
        print(' '.join(map(str, final_list)))
