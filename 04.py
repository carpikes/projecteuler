import math
def is_palindrome(n):
    s = str(n)
    l = math.ceil(len(s)/2)
    
    for i in range(0, l+1):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

max = 1
for i in range(100, 999):
    for j in range(100, 999):
        if is_palindrome(i*j):
            if i*j>max:
                max = i*j

print (max)
