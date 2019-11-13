

def multiply(pi1, pi2):
    result = {}
    for key in pi1:
        value = pi1[key]
        result[key] = pi2[value]
    return result


def pi_reversed(pi):
    result = {}
    for key, value in pi.items():
        result[value] = key
    return result


def generate_n_identity_permutation(n):
    result = {}
    for i in  range(1, n+1):
        result[i] = i
    return result


def power(pi1, k):

    if k < 0:
        base = pi_reversed(pi1)
    else:
        base = pi1

    abs_k = abs(k)

    result = base.copy()
    for i in range(1, abs_k):
        result = multiply(result, base)
    return result


def rank_naive(pi):
    n = len(pi)
    expected = generate_n_identity_permutation(n)
    if expected == pi:
        return 1

    k = 2
    result = multiply(pi, pi)

    while expected != result:
        k += 1
        result = multiply(result, pi)
    return k
