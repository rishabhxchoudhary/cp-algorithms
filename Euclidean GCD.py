from time import time
# Recursive Approach
def recur_GCD(a,b):
    if b==0:
        return a
    else:
        return recur_GCD(b,a%b)

# Iterative Approach
def iter_GCD(a,b):
    while b:
        a = a%b
        a,b=b,a
    return a
