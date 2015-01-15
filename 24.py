count = 0

def perm(x, y):
    global count
    if len(x) == 0:
        count += 1
        if count == 1000000:
            print(y)
            quit()
    else:
        for i in range(0, len(x)):
            perm(x[:i]+x[(i+1):],y+x[i])

perm("0123456789", "")
