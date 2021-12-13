import time

def isPrime(n):
    if n % 2 == 0: return False
    elif n < 2: return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def Twin_Primes(n, m):
    n = n if (n % 2) else (n + 1)
    res = []
    flag = False
    for i in range(n,m+1,2):
        if isPrime(i):
            if flag:
                res.append((i-2,i))
            else:
                flag = True
        else:
            flag = False
    return res

def Twin_Primes2(n, m):
    n = n if (n % 2) else (n + 1)
    res = []
    for i in range(n,m-1,2):
        if isPrime(i) and isPrime(i+2):
            res.append((i,i+2))
    return res               
    
    
n=2
m=1000000
a = time.time()
(sorted(Twin_Primes(n, m)))
b = time.time()
(sorted(Twin_Primes2(n, m)))
c = time.time()
print(b-a)
print(c-b)