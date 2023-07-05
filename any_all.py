n, ls = int(input()), list(map(int, input().split()))
print(all([i > 0 for i in ls]) and any([(i < 10 or i % 11 == 0) for i in ls]))

# 5
# 12 9 61 5 14 
# True

# Condition  
# If all the integers are positive, then you need to check if any integer is a palindromic integer.
# < 10 is single, so already palindrome, and % 11 is palindrome
