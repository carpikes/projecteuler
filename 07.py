import math
c = 2 # the 2nd prime number
n = 3 # is 3 (and 1?)

def is_prime(n):
    for i in range(3,round(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

while c != 10001:
    n += 2
    if is_prime(n):
        c += 1

print(n)    
