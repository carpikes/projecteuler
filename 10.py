import math
c = 2 # the 2nd prime number
n = 3 # is 3 (and 1?)

def is_prime(n):
    for i in range(3,round(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

sum = 2
max = 2*1000*1000

for i in range(3, max, 2):
    if is_prime(i):
        sum += i

print(sum)
