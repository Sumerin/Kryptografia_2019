import Krypto.Cipher as Cipher
import Krypto.Permutation as Pi
import Krypto.Modular_Arithmetic as Modular


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
    return None


def zad_4():
    a = pow(2, 16) - 1
    b = pow(2, 16) + 1

    result1 = Modular.nwd([a, b])
    print("nwd")
    print(result1)

    result2 = pow(a, 32) * pow(b, 32)  # nwd is 1
    print("nww")
    print(result2)

    # print(Modular.phi_by_kanon_pow(a, b))

def zad_5():
   return None


zad_1()
# zad_2()
# zad_3()
# zad_4()
# zad_5()
