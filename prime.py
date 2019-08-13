def prime(n):
    prme = [True]*(n+1)
    p = 2
    while p*p <=n:
        if prme[p] == True:
            for i in range(p*p,n+1,p):
                prme[i] = False
        p += 1
    count = 0
    for i in range(2,n+1):
        if prme[i] == True:
            count += 1
    return count
n = int(input())
print(prime(n))
