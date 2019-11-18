import math


import math
from functools import reduce
import numpy as np


def mul_modulo(a, b, mod):
    return ((a % mod) * (b % mod)) % mod


def pow_modulo(a, n, mod):
    return pow(a, n, mod)


def is_prime(a):
    r = math.floor(math.sqrt(a)) + 1
    for i in range(2, r):
        if a % i == 0:
            return False
    return True


def divisors(a):
    d = {1, a}
    for b in range(2, math.floor(math.sqrt(a)) + 1):
        "range do not include end value, +1 is necessary"
        if a % b == 0:
            d.add(b)
            d.add(int(a / b))
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


def nwd(list):
    x = reduce(np.gcd, list)
    return x


def nww(list):
    x = reduce(np.lcm, list)
    return x


def tau(a):
    return divisors_count(a)


def jota(a):
    if a == 0:
        return 1
    result = math.floor(math.log2(abs(a))) + 1
    return result


def phi(a):
    "Symbolem φ(a) oznaczamy liczbę tych liczb naturalnych, " \
    "które są mniejsze lub równe od liczby naturalnej a " \
    "i są z nią względnie pierwsze." \
    "φ nazywane jest funkcją Eulera. "
    "WIĘCEJ WŁAŚCIWOŚCI PATRZ SLAJDY 22, 26"
    if a > 1 and is_prime(a):
        return a - 1
    count = 0
    for i in range(1, a + 1):
        "range do not include end value, +1 is necessary"
        if np.gcd(i, a) == 1:
            count += 1
    return count


def phi_by_kanon(a):
    kanon_form = kanon(a)

    euler = 1
    for pk in kanon_form:
        ak = kanon_form[pk]
        tmp = pow(pk, ak) - pow(pk, ak - 1)
        euler *= tmp
    return euler


def phi_by_kanon2(a):
    kanon_form = kanon2(a)

    euler = 1
    for pk in kanon_form:
        ak = kanon_form[pk]
        tmp = pow(pk, ak) - pow(pk, ak - 1)
        euler *= tmp
    return euler


def phi_by_kanon_pow(a, b):
    kanon_form = kanon(a)

    euler = 1
    for pk in kanon_form:
        ak = kanon_form[pk] * b
        tmp = pow(pk, ak) - pow(pk, ak - 1)
        euler *= tmp
    return euler


def kanon(a):
    kanon_form = {}
    for i in range(2, a+1):
        if a == 1:
            break
        value = a / i
        if math.floor(value) == value:
            kanon_form[i] = 0
            while math.floor(value) == value:
                a = value
                kanon_form[i] += 1
                value = a / i
    return kanon_form


def kanon2(a):
    kanon_form = {}
    for i in range(2, a+1):
        if a == 1:
            break
        value = a % i
        if value == 0:
            kanon_form[i] = 0
            while value == 0:
                a = a / i
                kanon_form[i] += 1
                value = a % i
    return kanon_form


def pi(a):
    if a == 1:
        return 0
    if a == 2:
        return 1
    primes = [2]
    for i in range(3, a + 1, 2):
        is_i_prime = True
        for prime in primes:
            if i % prime == 0:
                is_i_prime = False
                break
        if is_i_prime:
            primes.append(i)
    return len(primes)


def pi_from_probability(n):
    if n <= 59:
        res = pi(n)
        return res, res

    lnn = math.log(n)
    t1 = n / lnn

    leftside = t1 + (t1 / (2*lnn))
    rightside = t1 + (t1 / ((2/3) * lnn))
    return leftside, rightside


def fermat(n):
    power = pow(2, n)
    return pow(2, power) + 1


def nfermat(a):
    n = 0
    fermat_base = pow(2, pow(2, n))
    fer = fermat_base + 1
    while fer < a:
        fermat_base *= fermat_base
        fer = fermat_base + 1
        n += 1
    if a == fer:
        return n
    else:
        return None


def nPrime(n):
    primes = [2]
    count = 1
    i = 3
    while count < n:
        is_i_prime = True
        for prime in primes:
            if i % prime == 0:
                is_i_prime = False
                break
        if is_i_prime:
            primes.append(i)
            count += 1
        i += 1
    return primes


def ModuloEquatation(a, b, mod, ran):
    result = []
    expected = b % mod

    for i in ran:
        value = mul_modulo(a, i, mod)
        if value == expected:
            result.append(i)

    return result


def euklidesEquatation(a, b):
    x, x_prim, y, y_prim = 1, 0, 0, 1
    while b != 0:
        q = math.floor(a/b)
        r = b
        b = a % b
        a = r

        t = x_prim
        x_prim = x - (q*x_prim)
        x = t

        t = y_prim
        y_prim = y - (q*y_prim)
        y = t
    return a, x, y
