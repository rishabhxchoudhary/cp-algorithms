def bin_exp(a,n):
    ans=1
    while n>0:
        if n&1:
            ans*=a
        a*=a
        n=n>>1
    return ans
