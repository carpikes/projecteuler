def fact(n):
    if n == 0: 
        return 1
    return n * fact(n-1)

n = 20

routes = round(fact(2*n) / (fact(n) ** 2))

print(routes)
