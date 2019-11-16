import Krypto.Cipher as Cipher
import Krypto.Permutation as Pi
import Krypto.Modular_Arithmetic as Modular


def zad_6():
    encrypted_full ="Róaniezoslbołżncynk irsepnżz izy z zipw iec"
    encrypted ="aa"
    key = ""

    for char in Cipher.letters:
        newKey = key + char
        m = len(newKey)
        result = Cipher.vigenere_decipher(encrypted, newKey, m)
        print(newKey)
        print(result)
        print()


def zad_1():
    p1 = {
        1:2,
        2: 4,
        3: 6,
        4: 8,
        5: 10,
        6: 1,
        7: 3,
        8: 5,
        9: 7,
        10: 9,
    }
    p2 = {
        1:1,
        2: 3,
        3: 5,
        4: 6,
        5: 9,
        6: 10,
        7: 8,
        8: 7,
        9: 4,
        10: 2,
    }

    p1p2 = Pi.multiply(p1, p2)
    print(p1p2)
    p2p1 = Pi.multiply(p2, p1)
    print(p2p1)


def zad_2():
    base = 2018
    power = 2018
    mod = pow(2, 32) - 1

    a = Modular.pow_modulo(base, power, mod)

    t1 = int(pow(2, 16) - 1)
    result1 = a % t1
    print(" a mod( 2^16 -1)")
    print(result1)

    result2 = Modular.tau(a)
    print(" tau(a)")
    print(result2)

    result3 = Modular.jota(a)
    print(" jota(a)")
    print(result3)

    result4 = Modular.nwd([a, t1])
    print(" nwd(a, 2^16 -1)")
    print(result4)

    result5 = Modular.nww([a, t1])
    print(" nww(a, 2^16 -1)")
    print(result5)

    # result6 = Modular.pi(a)
    # print(" pi(a)")
    # print(result6)

    result7 = Modular.phi_by_kanon(a)
    print(" euler(a)")
    print(result7)

    # result8 = Modular.phi_by_kanon(a)
    t2 = Modular.kanon(a)
    print(" zad2.1")
    # print(result8)
    print(min(t2))

    result9 = Modular.nfermat(a)
    print(" zad2.2")
    print(result9)
    print(t2)




# zad_1()
zad_2()

# zad_6()