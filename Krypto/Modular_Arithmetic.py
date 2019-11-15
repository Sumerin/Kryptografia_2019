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


def divisors(a):
    d = {1, a}
    for b in range(2, math.floor(math.sqrt(a))+1):
        "range do not include end value, +1 is necessary"
        if a % b == 0:
            d.add(b)
            d.add(int(a/b))
    return d


def divisors_count(a):
    if a == 1:
        return 1
    d = 2
    for b in range(2, math.floor(math.sqrt(a)) + 1):
        "range do not include end value, +1 is necessary"
        if a % b == 0:
            d += 2
    return d

