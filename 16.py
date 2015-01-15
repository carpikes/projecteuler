
def sum(n):
    s = str(n)
    sx = 0
    for i in s:
        sx += int(i)
    return sx;

print(sum(2**1000))

