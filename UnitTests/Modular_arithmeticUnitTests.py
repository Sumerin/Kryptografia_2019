import unittest
import math
import Krypto.Modular_Arithmetic as Modular


class Modular_ArithmeticMethods(unittest.TestCase):

    def test_pow_modulo(self):
        expected = 2110863454

        a = 2018
        n = 2018
        mod = pow(2, 32) - 1

        result = Modular.pow_modulo(a, n, mod)
        self.assertEquals(expected, result)

    def test_tau(self):
        expected = 6
        a = 32

        result = Modular.tau(a)
        self.assertEquals(expected, result)

    def test_tau2(self):
        expected = 8
        a = 30

        result = Modular.tau(a)
        self.assertEquals(expected, result)

    def test_jota(self):
        expected = 1
        a = 0

        result = Modular.jota(a)
        self.assertEquals(expected, result)

    def test_jota_positive(self):
        expected = 3
        a = 5

        result = Modular.jota(a)
        self.assertEquals(expected, result)

    def test_jota_negative(self):
        expected = 3
        a = -5

        result = Modular.jota(a)
        self.assertEquals(expected, result)

    def test_is_prime_true(self):
        self.assertTrue(Modular.is_prime(1))
        self.assertTrue(Modular.is_prime(2))
        self.assertTrue(Modular.is_prime(3))
        self.assertTrue(Modular.is_prime(5))
        self.assertTrue(Modular.is_prime(pow(2, 16) + 1))

    def test_is_prime_false(self):
        self.assertFalse(Modular.is_prime(4))
        self.assertFalse(Modular.is_prime(6))
        self.assertFalse(Modular.is_prime(8))
        self.assertFalse(Modular.is_prime(pow(2, 16) - 1))
        self.assertFalse(Modular.is_prime(pow(3, 16) - 1))

    def test_NWD1(self):
        expected = 1
        a = 5
        b = 12
        self.assertEquals(expected, Modular.nwd(a, b))

    def test_NWD2(self):
        expected = 1
        a = math.pow(2, 16) + 1
        b = math.pow(2, 16) - 1
        self.assertEquals(expected, Modular.nwd(a, b))

    def test_NWD3(self):
        t1 = Modular.nwd(6, 8)
        t2 = Modular.nwd(6*6, 8*8)
        expected = 6
        a = 24
        b = 18
        self.assertEquals(expected, Modular.nwd(a, b))

    def test_NWW1(self):
        a = 5
        b = 12
        expected = a * b
        self.assertEquals(expected, Modular.nww(a, b))

    def test_NWW2(self):
        a = math.pow(2, 16) + 1
        b = math.pow(2, 16) - 1
        expected = a * b
        self.assertEquals(expected, Modular.nww(a, b))

    def test_NWW3(self):
        expected = 72
        a = 24
        b = 18
        self.assertEquals(expected, Modular.nww(a, b))

    def test_euler1(self):
        expected = 4
        a = 10
        self.assertEquals(expected, Modular.euler(a))

    def test_euler2(self):
        expected = 6
        a = 9
        self.assertEquals(expected, Modular.euler(a))

    def test_euler3(self):
        expected = math.pow(2, 16)
        a = math.pow(2, 16) + 1
        self.assertEquals(expected, Modular.euler(a))

    def test_euler4(self):
        expected = 1
        a = 1
        self.assertEquals(expected, Modular.euler(a))
