
def d(n):
    s = 0
    for i in range(1, round(n/2)+1):
        if n % i == 0:
            s += i
    return s

def f(n):
    dx = d(n)
    if n == dx:
        return False
    bx = d(dx)
    if(bx == n):
        return True
    return False

sum = 0
for i in range(1,10000):
    if f(i):
        sum += i

print(sum)
