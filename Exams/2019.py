import Krypto.Cipher as Cipher
import Krypto.Permutation as Pi
import Krypto.Modular_Arithmetic as Modular
import numpy as np


def zad_1():
    a1 = {
        1:2,
        2: 3,
        3: 1,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
    }
    pi ={
        1: 3,
        2: 1,
        3: 2,
        4: 5,
        5: 4,
        6: 7,
        7: 6,
    }
    a2 = {
        1: 1,
        2: 2,
        3: 3,
        4: 5,
        5: 4,
        6: 6,
        7: 7,
    }

    ares = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 7,
        7: 6,
    }

    result = Pi.multiply(Pi.multiply(a1, pi), a2)

    if result == ares:
        print("pi is correct")

    result1 = pi[1]
    result11 = Pi.rank_naive(pi)
    print("Pi")
    print(result1)
    print(result11)

    t2 = Pi.pi_reversed(pi)
    result2 = t2[1]
    result22 = Pi.rank_naive(t2)
    print("Pi^-1")
    print(result2)
    print(result22)

    t3 = Pi.power(pi, 2)
    result3 = t3[1]
    result33 = Pi.rank_naive(t3)
    print("Pi^2")
    print(result3)
    print(result33)


def zad_2():
    message = "LICZBA WYSOCE ZŁOŻONA"

    result1 = Cipher.railFence_encipher(message, 3)
    print("1")
    print(result1)

    result2 = Cipher.matrix_cipher(message, 3)
    print("2")
    print(result2)

    result3 = Cipher.column_encipher(message, "NWD")
    print("3")
    print(result3)

    result4 = Cipher.vigenere_encipher(message, "NWW", len("NWW"))
    print("4")
    print(result4)

    result5 = Cipher.cesar(message)
    print("5")
    print(result5)


def zad_3():
    n = 5
    solutions = []
    primes = Modular.nPrime(n)
    ran = range(1, 2048)
    for i in range(1, n + 1):
        solutions.append(Modular.ModuloEquatation(1, i, primes[i - 1], ran))

    base = set(solutions[0])
    for i in range(1, n):
        B = set(solutions[i])
        base = base.intersection(B)

    x = min(base)

    print(x)
    is_prime = Modular.is_prime(x)
    print("is prime:", is_prime)

    result1 = Modular.tau(x)
    print(result1)

    result2 = Modular.phi(x)
    print(result2)

    result3 = Modular.jota(x)
    print(result3)

    result4 = Modular.kanon(x)
    print(result4)


def zad_4():
    a = pow(2, 16) - 1
    b = pow(2, 16) + 1

    result1 = Modular.nwd([a, b])
    print("nwd")
    print(result1)

    result2 = pow(a, 32) * pow(b, 32)  # nwd is 1
    print("nww")
    print(result2)

    print(Modular.phi_by_kanon_pow(a, b))


def zad_5():
    ran = range(0, 1024)
    result0 = Modular.ModuloEquatation(8, 8, 1024, ran)

    print("NWD")
    print(Modular.nwd(result0))

    print('Sum of x')
    print(np.sum(result0))

    max_value = 0
    max_power = 0
    for i in range(len(result0)):
        value = result0[i]
        power = Modular.phi(value)
        if max_power < power:
            max_power = power
            max_value = value
        elif power < max_power:
            a = pow(max_value, max_power)
            b = pow(value, power)
            if a < b:
                max_power = power
                max_value = value

    print("max")
    print(pow(max_value, max_power))

    print('k')
    print(len(result0))


# zad_1()
# zad_2()
# zad_3()
# zad_4()
zad_5()
