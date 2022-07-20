def hash(s):
    p=31
    m=1e9+9
    hash_val = 0
    p_pow = 1
    for c in s:
        hash_val = (hash_val + (ord(c) - ord('a') + 1)*(p_pow) )% m
        p_pow = (p_pow*p) % m
    return hash_val
