
abcache = {}
def div(n):
    global abcache

    if n in abcache:
        return abcache[n]
    else:
        sum=0
        for i in range(1, round(n/2)+1):
            if n % i == 0:
                sum += i
        
        k = sum-n

        ret = 1 if sum-n > 0 else -1 if sum-n < 0 else 0
        abcache[n]=ret
        return ret

sum = 0
for i in range(1, 28123):
    summable = True
    for j in range(1, i-11):
        k = i - j
        dj = div(j)
        dk = div(k)
        
        if div(j)>0 and div(k)>0:
            summable = False
            break

    if summable:
        print(i)
        sum += i

print(sum)
