
def gcd(a, b, *add_num):
    """Computes the gcd of two or more numbers"""
    assert(isinstance(a, int))
    assert(isinstance(b, int))
    assert(a >= 0)
    assert(b >= 0)
    if len(add_num) > 0:
        return gcd(gcd(a, b), *add_num)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b, *add_num):
    """Computes the lcm of two or more numbers"""
    assert(isinstance(a, int))
    assert(isinstance(b, int))
    assert(a >= 0)
    assert(b >= 0)
    if len(add_num) > 0:
        return lcm(lcm(a, b), *add_num)
    return abs(a * b) // gcd(a, b)

def modinv(n, m):
    """Computes the modular inverse of a number n modulo m"""
    assert(isinstance(n, int))
    assert(isinstance(m, int))
    assert(n >= 0)
    assert(m >= 0)
    gcd, x, y = eea_helper(n, m)
    if gcd != 1:
        raise ValueError(f"No modular Inverse exists for {n} modulo {m}")
    else:
        return x % m

def eea(a, b):
    """Computes the extended gcd of a and b"""
    assert(isinstance(a, int))
    assert(isinstance(b, int))
    assert(a >= 0)
    assert(b >= 0)
    if b == 0:
        return f"({a} * 1) + ({b} * 0) = {a}"
    gcd, x1, y1 = eea_helper(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return f"({a} * {x}) + ({b} * {y}) = {gcd}"

def eea_helper(a, b):
    """Helper function to compute the extended gcd of 2 numbers"""
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = eea_helper(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y
