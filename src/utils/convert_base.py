
def bin2dec(binary_str):
    """Converts a binary string to a decimal integer."""
    return int(binary_str, 2)

def dec2bin(decimal_int):
    """Converts a decimal integer to a binary string."""
    return bin(decimal_int)[2:]  # Removes the '0b' prefix

def hex2dec(hex_str):
    """Converts a hexadecimal string to a decimal integer."""
    return int(hex_str, 16)

def dec2hex(decimal_int):
    """Converts a decimal integer to a hexadecimal string."""
    return hex(decimal_int)[2:]  # Removes the '0x' prefix

def oct2dec(octal_str):
    """Converts an octal string to a decimal integer."""
    return int(octal_str, 8)

def dec2oct(decimal_int):
    """Converts a decimal integer to an octal string."""
    return oct(decimal_int)[2:]  # Removes the '0o' prefix

def bin2hex(binary_str):
    """Converts a binary string to a hexadecimal string."""
    decimal = bin2dec(binary_str)
    return dec2hex(decimal)

def hex2bin(hex_str):
    """Converts a hexadecimal string to a binary string."""
    decimal = hex2dec(hex_str)
    return dec2bin(decimal)

def bin2oct(binary_str):
    """Converts a binary string to an octal string."""
    decimal = bin2dec(binary_str)
    return dec2oct(decimal)

def oct2bin(octal_str):
    """Converts an octal string to a binary string."""
    decimal = oct2dec(octal_str)
    return dec2bin(decimal)

def hex2oct(hex_str):
    """Converts a hexadecimal string to an octal string."""
    decimal = hex2dec(hex_str)
    return dec2oct(decimal)

def oct2hex(octal_str):
    """Converts an octal string to a hexadecimal string."""
    decimal = oct2dec(octal_str)
    return dec2hex(decimal)

