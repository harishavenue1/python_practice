# Enter your code here. Read input from STDIN. Print output to STDOUT
n, ls = int(input()), list(map(int, input().split()))
print(all([i > 0 for i in ls]) and any([(i < 10 or i % 11 == 0) for i in ls]))
