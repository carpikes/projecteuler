
def col(n):
    if n<3:
        return 1

    sum = 0
    q = n*n
    for i in range(0,4):
        sum = sum + q
        q = q - (n-1)
    return sum + col(n-2)

print(col(1001))
