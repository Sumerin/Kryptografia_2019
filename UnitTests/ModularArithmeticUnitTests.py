import unittest
import Krypto.Modular_Arithmetic as MA


class ModularArithmeticMethods(unittest.TestCase):

    def test_simple_multiply(self):
        expected = 1
        result = MA.mul_modulo(2, 3, 5)
        self.assertEqual(expected, result)

    def test_multiply_by_modulo_multiple(self):
        expected = 0
        result = MA.mul_modulo(10, 7, 5)
        self.assertEqual(expected, result)

    def test_multiply_large_numbers(self):
        expected = 28459179
        first = pow(81723, 4)
        second = pow(56789, 7)
        mod = 123456789
        result = MA.mul_modulo(first, second, mod)
        self.assertEqual(expected, result)

    def test_simple_power(self):
        expected = 4
        first = 5
        second = 4
        mod = 9
        result = MA.pow_modulo(first, second, mod)
        self.assertEqual(expected, result)

    def test_power_large_numbers(self):
        expected = 2110863454
        first = 2018
        second = 2018
        mod = pow(2, 32) - 1
        result = MA.pow_modulo(first, second, mod)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()