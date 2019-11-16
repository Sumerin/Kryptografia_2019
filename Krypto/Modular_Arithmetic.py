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


def kanon(a):
    kanon_form = {}
    for i in range(2, math.floor(math.sqrt(a)) + 1):
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


def pi(a):
    count = 1
    if a == 1:
        return 0
    if a == 2:
        return 1
    for i in range(3, a+1, 2):
        if is_prime(i):
            count += 1
    return count



