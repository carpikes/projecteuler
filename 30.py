
def check(i):
    sum = 0
    a = i
    while i > 0:
        sum += (i%10) ** 5
        i /= 10
    if sum == a:
        return True
    else:
        return False

sum = 0
for i in range(1000,1000000):
    if check(i):
        sum += i
        print(i)

print("--")
print(sum)
