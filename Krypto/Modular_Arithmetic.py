import math


def mul_modulo(a,b, mod):
    return ((a % mod) * (b % mod)) % mod


def pow_modulo(a, n, mod):
    c = 1
    while n > 0:
        if not n % 2 == 0:
            c = mul_modulo(c, a, mod)
        a = mul_modulo(a, a, mod)
        n = math.floor(n/2)
    return c