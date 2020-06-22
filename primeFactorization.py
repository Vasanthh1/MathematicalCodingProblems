from math import sqrt
from collections import Counter

def primeFactorsWithPower(n):
    l = []
    while n%2 == 0:
        l.append(2)
        n//=2
    for i in range(3,int(sqrt(n))+1):
        while n%i==0:
            l.append(i)
            n//=i
    if n>2:
        l.append(n)
    l = Counter(l)
    for i in l:
        print(i,l[i])
primeFactorsWithPower(int(input()))
