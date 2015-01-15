
def readfile(name):
    f = open(name, "r")
    n = []
    for line in f:
        line = line[0:len(line)-1]
        if len(line) == 50:
            n.append(int(line))
    f.close()
    return n

n = readfile("in/13.txt")

sum = 0
for i in range(0, len(n)):
    sum += n[i]

sum = str(sum)[:10]
print(sum)
