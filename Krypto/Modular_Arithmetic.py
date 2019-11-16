import math


def mul_modulo(a, b, mod):
    return ((a % mod) * (b % mod)) % mod


def pow_modulo(a, n, mod):
    c = 1
    while n > 0:
        if not n % 2 == 0:
            c = mul_modulo(c, a, mod)
        a = mul_modulo(a, a, mod)
        n = math.floor(n/2)
    return c


def tau(a):
    result = 1
    for b in range(1, a):
        t1 = math.floor(a / b)
        t2 = math.floor((a - 1) / b)
        result += (t1 - t2)

    return result


def jota(a):
    if a == 0:
        return 1
    result = math.floor(math.log2(abs(a))) + 1
    return result


def is_prime(a):
    r = math.floor(math.sqrt(a)) + 1
    for i in range(2, r):
        if a % i == 0:
            return False
    return True

def jota(a):
    if a == 0:
        return 1
    result = math.floor(math.log2(abs(a))) + 1
    return result


def is_prime(a):
    r = math.floor(math.sqrt(a)) + 1
    for i in range(2, r):
        if a % i == 0:
            return False
    return True


def nwd(a, b):
    while b != 0:
        pom = a % b
        a = b
        b = pom
    return a


def nww(a, b):
    d = nwd(a, b)
    result = 0
    if a > b:
        result = a / d * b
    else:
        result = b / d * a
    return result


def euler(a):
    if a > 1 and is_prime(a):
        return a - 1
    result = 0
    for i in range(1, a + 1):
        if nwd(a, i) == 1:
            result += 1
    return result
