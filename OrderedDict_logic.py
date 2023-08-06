from collections import OrderedDict

dic = OrderedDict()
for _ in range(int(input())):
    *k, v = input().split()
    dic[' '.join(k)] = dic.get(' '.join(k), 0) + int(v)

for k, v in dic.items():
    print(k, v)
