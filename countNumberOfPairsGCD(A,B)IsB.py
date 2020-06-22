def countNumberOfGcdOf_a_b_is_b(n):
    ans = 0
    for i in range(1,n+1):
        temp = n//i
        if temp == 1:
            return ans+n-i+1
        else:
            ans += temp
    return ans
print(countNumberOfGcdOf_a_b_is_b(int(input())))
