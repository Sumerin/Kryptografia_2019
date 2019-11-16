import math
from functools import reduce
import numpy as np


def mul_modulo(a, b, mod):
    return ((a % mod) * (b % mod)) % mod


def pow_modulo(a, n, mod):
    return pow(a, n, mod)


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


def phi(a):
    "Symbolem φ(a) oznaczamy liczbę tych liczb naturalnych, " \
    "które są mniejsze lub równe od liczby naturalnej a " \
    "i są z nią względnie pierwsze." \
    "φ nazywane jest funkcją Eulera. "
    "WIĘCEJ WŁAŚCIWOŚCI PATRZ SLAJDY 22, 26"
    count = 0
    for i in range(1, a + 1):
        "range do not include end value, +1 is necessary"
        if np.gcd(i, a) == 1:
            count += 1
    return count