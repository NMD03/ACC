import random

def isprime(n):
    """Checks if the given number is prime using the Miller-Rabin-Test"""
    assert(isinstance(n, int))
    assert(n > 0)
    NUMBER_OF_CYCLES = 20

    # Filter out obvious numbers for speed up
    SMALL_PRIMES = [2, 3, 5, 7]
    if n in SMALL_PRIMES:
        return True
    elif ((n % 2) == 0) or (n < SMALL_PRIMES[-1]):
        return False
    
    def miller_rabin_pass(a, s, d, n):
        """Core Miller-Rabin-Test that computes if n is prime with accuracy > 3/4"""
        x  = pow(a, d, n)
        if x == 1 or x == n-1:
            return True
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n-1:
                return True
        return False
    
    # Get parameters for Miller-Rabin-Test
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # Perform Miller-Rabin-Test
    for _ in range(NUMBER_OF_CYCLES):
        a = random.randint(2, n - 2)
        if not miller_rabin_pass(a, s, d, n):
            return False

    return True

def nextprime(n):
    """Returns the next prime greater or equal to n"""
    assert(isinstance(n, int))
    assert(n > 0)
    if (n % 2) == 0:
        n += 1 
    while not isprime(n):
        n += 2
    return n


