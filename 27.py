numbers = {}

def is_prime(n):
    global numbers

    if n < 0:
        return False

    if n in numbers:
        return numbers[n]

    if n % 2 == 0:
        numbers[n] = False
        return False

    for i in range(3, round(n/2) + 1, 2):
        if n % i == 0:
            numbers[n] = False
            return False

    numbers[n] = True
    return True

def check_primes(a,b):
    n_primes = 0
    n = 1
    while True:
        num = n*n + a*n + b
        if is_prime(num):
            n += 1
        else:
            return n 

max = 0
ma = 0
mb = 0
for a in range(-1000, 1000):
    for b in range(1, 1000):
        if is_prime(b):
            npr = check_primes(a,b)
            if npr>max:
                max = npr
                ma = a
                mb = b

#print(max)
#print(str(ma) + ";" + str(mb) + ";" + str(ma*mb))
print(str(ma*mb))
