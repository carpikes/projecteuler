import math

n = 600851475143

# -----

if n % 2 == 0:
    n /= 2

max = 1

for i in range(3, math.ceil(n/2), 2):
    if n == 1:
        break
    if n % i == 0:
        max = i
        n /= i

if max == 1:
    max = n

print (max)
