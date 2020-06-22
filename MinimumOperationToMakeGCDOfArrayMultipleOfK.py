'''Minimum operations to make GCD of array a multiple of k'''

def minimumOperationToMakeMultipleOfK(l,k):
    n = len(l)
    l = [i%k for i in l]
    ans = 0
    for i in l:
        ans += min(i,k-i)
    return ans
print(minimumOperationToMakeMultipleOfK(list(map(int,input().split())),int(input())))
    
