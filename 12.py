def ndiv(n):
    c=0
    limit=n
    i=1
    while i < limit:
        if n % i == 0:
            limit = n / i
            if limit != i:
                c+=1
            c+=1
        i+=1
    return c

def tri(n):
    sum = 0
    for i in range(1, n):
        sum += i
    return sum

i = 1
n = 0
max = 1
while True:
    n += i
    d = ndiv(n)

#    print(str(n) + ";" + str(d))

    if d > max:
        max = d
        print(max)
    if d > 500:
        print(n)
        break
    i += 1
