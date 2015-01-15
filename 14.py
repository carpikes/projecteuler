
def collatz(n):
    i = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        i=i+1
    return i

max = 1
mn = 1
for i in range(0, 1000000):
    k = collatz(i)
    if k>max:
        max = k
        mn = i
        print(str(max) + ";" + str(mn))

print(mn)
