import math 

def nCr(n, r):
    """Compute the combinations of r out of n"""
    return math.comb(n, r)

def nPr(n, r):
    """Compute the permutations of r out of n"""
    return math.perm(n, r)

def factorial(n):
    """Compute the factorial of x (x!)"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
