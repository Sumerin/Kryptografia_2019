import unittest
import Krypto.Permutation as Pi


class PermutationMethods(unittest.TestCase):

    def test_simple_multiply(self):
        expected = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
        }

        permutation = {
            1: 2,
            2: 1,
            3: 4,
            4: 3,
        }
        result = Pi.multiply(permutation, permutation)
        self.assertDictEqual(expected, result)

    def test_multiply_StatePoint(self):
        expected = {
            1: 1,
            2: 4,
            3: 2,
            4: 3,
        }

        permutation = {
            1: 1,
            2: 3,
            3: 4,
            4: 2,
        }
        result = Pi.multiply(permutation, permutation)
        self.assertDictEqual(expected, result)

    def test_power_positive(self):
        expected = {
            1: 1,
            2: 5,
            3: 6,
            4: 2,
            5: 3,
            6: 4
        }

        permutation = {
            1: 1,
            2: 3,
            3: 4,
            4: 5,
            5: 6,
            6: 2
        }

        result = Pi.power(permutation, 3)
        self.assertDictEqual(expected, result)

    def test_pi_reversed(self):
        expected = {
            2: 1,
            3: 2,
            1: 3,
        }

        permutation = {
            1: 2,
            2: 3,
            3: 1
        }

        result = Pi.pi_reversed(permutation)
        self.assertDictEqual(expected, result)

    def test_power_negative(self):
        expected = {
            1: 2,
            2: 3,
            3: 1,
        }

        permutation = {
            1: 2,
            2: 3,
            3: 1
        }

        result = Pi.power(permutation, -2)
        self.assertDictEqual(expected, result)

    def test_rank_naive_1(self):
        expected = 1

        permutation = {
            1: 1,
            2: 2,
            3: 3
        }

        result = Pi.rank_naive(permutation)
        self.assertEquals(expected, result)

    def test_rank_naive_2(self):
        expected = 2

        permutation = {
            1: 2,
            2: 1,
            3: 4,
            4: 3
        }

        result = Pi.rank_naive(permutation)
        self.assertEquals(expected, result)

    def test_rank_naive_3(self):
        expected = 3

        permutation = {
            1: 2,
            2: 3,
            3: 1
        }

        result = Pi.rank_naive(permutation)
        self.assertEquals(expected, result)


if __name__ == '__main__':
    unittest.main()
