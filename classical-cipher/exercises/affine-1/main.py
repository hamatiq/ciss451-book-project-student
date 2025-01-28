def gcd(a, b):
    """Calculate the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find x, y such that ax + by = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def multiplicative_inverse(a, mod):
    """Find the multiplicative inverse of a modulo mod."""
    gcd_value, x, _ = extended_gcd(a, mod)
    if gcd_value != 1:
        return None  # No inverse exists
    return x % mod

# Generate the table
mod = 26
table = []
for a in range(1, mod):
    inverse = multiplicative_inverse(a, mod)
    table.append((a, inverse))

# Print the results
print("a    a^(-1) mod 26")
for a, inv in table:
    if inv is None:
        print(f"{a:2}   None (not invertible)")
    else:
        print(f"{a:2}   {inv:2}")
