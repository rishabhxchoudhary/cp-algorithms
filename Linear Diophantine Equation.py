def extended_gcd(a,b):
    if b==0:
        return a,1,0
    g,x1,y1 = extended_gcd(b,a%b)
    x = y1
    y = x1 - int(a/b)*y1
    return g,x,y

# Given some a b and c find one solution:
def LDE(a,b,c):
    if a==0 and b==0:
        if c==0:
            return 1e9
        else:
            return 0
    g ,xg ,yg = extended_gcd(abs(a),abs(b))
    if (c%g!=0):
        return 0
    x0 = xg*(c//g)
    y0 = yg*(c//g)
    if a<0:
        x0 = -x0
    if b<0:
        y0=-y0
    return x0,y0

# -3x+4y = 7
print(LDE(-3,4,7))
