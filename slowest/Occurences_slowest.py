size_a, size_b = map(int, input().split())
list_a = [input().strip() for _ in range(int(size_a))]

for _ in range(size_b):
    c = input().strip()                 # don't use input in loops - slows down
    for idx, c1 in enumerate(list_a):
        if list_a.count(c) == 0:        # don't use many conditions in loops - slows down
            print(-1, end=' ')          # don't use print in loops - slows down
            break
        if c == c1:
            print(idx + 1, end=' ')
    print(end='\n')
