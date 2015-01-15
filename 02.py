
a = 0
b = 1
n = 1
s = 0
while n < 4*1000*1000:
    n = a + b
    if n % 2 == 0 and n < 4*1000*1000:
        s += n
    a = b
    b = n

print (s)
