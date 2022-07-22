# return both gcd and values of x and y
def extended_gcd(a,b):
    if b==0:
        return a,1,0
    g,x1,y1 = extended_gcd(b,a%b)
    x = y1
    y = x1 - int(a/b)*y1
    return g,x,y

print(extended_gcd(5,3))
