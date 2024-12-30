
def ror(value, shift, size=32):
    """Returns the rotated bits of value by shift using a right rotation in a register of size."""
    shift %= size
    mask = (1 << bit_size) - 1
    rotated = (value >> shift) | ((value << (bit_size - shift)) & mask)
    return rotated & mask

def rol(value, shift, size=32):
    """Returns the rotated bits of value by shift using a left rotation in a register of size."""
    shift %= size
    mask = (1 << bit_size) - 1
    rotated = ((value << shift) & mask) | (value >> (bit_size - shift))
    return rotated & mask

def xor(a ,b):
    """Returns the xor value of two byte arrays a and b"""
    Assert(len(a) == len(b))
    return bytes(ba ^ bb for ba, bb in zip(a, b))
