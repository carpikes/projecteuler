def readfile(name):
    f = open(name, "r")
    n = [[0 for x in range(20)] for x in range(20)]
    i = 0
    for line in f:
        el = line.split(" ")
        j = 0
        for c in el:
            if c != '\n':
                n[i][j] = int(c)
            j+=1
        i+=1
    f.close()
    return n

n = readfile("in/11.txt")
k = 4

max = 1
for i in range(0, 20):
    if i < 20-k+1:
        diag = True
    else:
        diag = False

    if i >= k:
        diagR = True
    else:
        diagR = False

    for j in range(0, 20-k+1):
        ph = 1
        pv = 1
        pd = 1
        pdr= 1
        for l in range(0, k):
            ph *= n[i][j+l]
            pv *= n[j+l][i]
            if diag:
                pd *= n[i+l][j+l]
            if diagR:
                pdr *= n[i-l][j+l]
        if ph>max:
            max = ph
        if pv>max:
            max = pv
        if pd>max:
            max = pd
        if pdr>max:
            max = pdr

print (max)
