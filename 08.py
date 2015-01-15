def readfile(name):
    f = open(name, "r")
    n = ""
    for line in f:
        for c in line:
            if c.isdigit():
                n += c
    f.close()
    return n

def mult(n):
    mult = 1
    for i in range(0,len(n)):
        mult *= int(n[i])
    return mult

n = readfile("in/8.txt")
g = 13

max = 0
for i in range(0, len(n)-g):
    l = n[i:i+g]
    m = mult(l)
    if(m>max):
        max = m

print(max)
