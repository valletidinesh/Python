def sexyPrime(m,n):
    prime = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if prime[p] == True:
            for i in range(p*p,n+1,p):
                prime[i] = False
        p += 1
    pair = 0
    for i in range(m,n-5):
        if prime[i] and prime[i+6]:
            pair += 1
    return pair

m = int(input())
n = int(input())
if m>=2 and n<=10**9:
    print(sexyPrime(m,n))
