# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

no_of_shoes = int(input())

shoe_coln = Counter(map(int, input().split()))

no_of_customers = int(input())

money = 0

for _ in range(no_of_customers):
    size, value = map(int, input().split())
    if shoe_coln[size] > 0:
        money += value
        shoe_coln.subtract(Counter([size]))

print(money)
