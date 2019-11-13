

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
