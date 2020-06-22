from math import sqrt
from collections import Counter

def KthPrimeOfaNumber(n,k):
    if n%2 ==0:
        k-=1
    if k==0:
        return 2
    while n%2 == 0:
        l.append(2)
        n//=2
    
    for i in range(3,int(sqrt(n))+1):
        if n%i ==0:
            k-=1
        while n%i==0:
            n//=i
        if k==0:
            return i
        
    if n>2:
        k-=1
        if k==0:
            return n
    return -1

print(KthPrimeOfaNumber(*list(map(int,input().split()))))
