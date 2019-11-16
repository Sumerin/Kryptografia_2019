import unittest
import math
import Krypto.Modular_Arithmetic as Modular


class Modular_ArithmeticMethods(unittest.TestCase):

    def test_simple_multiply(self):
        first = 2
        second = 3
        mod = 5
        result = Modular.mul_modulo(first, second, mod)
        expected = 1
        self.assertEqual(expected, result)

    def test_multiply_by_modulo_multiple(self):
        first = 10
        second = 7
        mod = 5
        result = Modular.mul_modulo(first, second, mod)
        expected = 0
        self.assertEqual(expected, result)

    def test_multiply_large_numbers(self):
        first = pow(81723, 4)
        second = pow(56789, 7)
        mod = 123456789
        result = Modular.mul_modulo(first, second, mod)
        expected = 28459179
        self.assertEqual(expected, result)

    def test_simple_power(self):
        first = 5
        second = 4
        mod = 9
        result = Modular.pow_modulo(first, second, mod)
        expected = 4
        self.assertEqual(expected, result)

    def test_power_large_numbers(self):
        first = 2018
        second = 2018
        mod = pow(2, 32) - 1
        result = Modular.pow_modulo(first, second, mod)
        expected = 2110863454
        self.assertEqual(expected, result)

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

    def test_NWD1(self):
        expected = 1
        a = 5
        b = 12
        self.assertEquals(expected, Modular.nwd([a, b]))

    def test_NWD2(self):
        expected = 1
        a = int(math.pow(2, 16) + 1)
        b = int(math.pow(2, 16) - 1)
        self.assertEquals(expected, Modular.nwd([a, b]))

    def test_NWD3(self):
        expected = 6
        a = 24
        b = 18
        self.assertEquals(expected, Modular.nwd([a, b]))

    def test_simple_nwd(self):
        arg = [12, 3, 48]
        result = Modular.nwd(arg)
        expected = 3
        self.assertEqual(expected, result)

    def test_simple_nwd_coprime(self):
        arg = [48, 25]
        result = Modular.nwd(arg)
        expected = 1
        self.assertEqual(expected, result)

    def test_simple_nwd_one_number(self):
        arg = [48]
        result = Modular.nwd(arg)
        expected = 48
        self.assertEqual(expected, result)

    def test_NWW1(self):
        a = 5
        b = 12
        expected = a * b
        self.assertEquals(expected, Modular.nww([a, b]))

    def test_NWW2(self):
        a = int(math.pow(2, 16) + 1)
        b = int(math.pow(2, 16) - 1)
        expected = a * b
        self.assertEquals(expected, Modular.nww([a, b]))

    def test_NWW3(self):
        expected = 72
        a = 24
        b = 18
        self.assertEquals(expected, Modular.nww([a, b]))

    def test_simple_nww(self):
        arg = [12, 3, 48, 7]
        result = Modular.nww(arg)
        expected = 336
        self.assertEqual(expected, result)

    def test_simple_nww_coprime(self):
        arg = [48, 25]
        result = Modular.nww(arg)
        expected = 1200
        self.assertEqual(expected, result)

    def test_simple_nww_one_number(self):
        arg = [48]
        result = Modular.nww(arg)
        expected = 48
        self.assertEqual(expected, result)

    def test_euler1(self):
        expected = 4
        a = 10
        self.assertEquals(expected, Modular.phi(a))

    def test_euler2(self):
        expected = 6
        a = 9
        self.assertEquals(expected, Modular.phi(a))

    def test_euler3(self):
        expected = math.pow(2, 16)
        a = int(math.pow(2, 16) + 1)
        self.assertEquals(expected, Modular.phi(a))

    def test_euler4(self):
        expected = 1
        a = 1
        self.assertEquals(expected, Modular.phi(a))

    def test_phi_prime(self):
        arg = 199
        result = Modular.phi(arg)
        expected = 198
        self.assertEqual(expected, result)

    def test_simple_phi(self):
        arg = 20
        result = Modular.phi(arg)
        expected = 8
        self.assertEqual(expected, result)

    def test_phi_prime(self):
        arg = 199
        result = Modular.phi(arg)
        expected = 198
        self.assertEqual(expected, result)

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

    def test_simple_divisors(self):
        arg = 24
        result = Modular.divisors(arg)
        expected = {1, 2, 3, 4, 6, 8, 12, 24}
        self.assertEqual(expected, result)

    def test_divisors_of_one(self):
        arg = 1
        result = Modular.divisors(arg)
        expected = {1}
        self.assertEqual(expected, result)

    def test_divisors_of_two(self):
        arg = 2
        result = Modular.divisors(arg)
        expected = {1, 2}
        self.assertEqual(expected, result)

    def test_simple_divisors_large_numbers(self):
        arg = 630504000
        result = Modular.divisors(arg)
        expected = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40, 42,
                    45, 48, 50, 54, 56, 60, 63, 64, 70, 72, 75, 80, 81, 84, 90, 96, 100, 105, 108, 112, 120, 125, 126,
                    135, 139, 140, 144, 150, 160, 162, 168, 175, 180, 189, 192, 200, 210, 216, 224, 225, 240, 250, 252,
                    270, 278, 280, 288, 300, 315, 320, 324, 336, 350, 360, 375, 378, 400, 405, 417, 420, 432, 448, 450,
                    480, 500, 504, 525, 540, 556, 560, 567, 576, 600, 630, 648, 672, 675, 695, 700, 720, 750, 756, 800,
                    810, 834, 840, 864, 875, 900, 945, 960, 973, 1000, 1008, 1050, 1080, 1112, 1120, 1125, 1134, 1200,
                    1251, 1260, 1296, 1344, 1350, 1390, 1400, 1440, 1500, 1512, 1575, 1600, 1620, 1668, 1680, 1728,
                    1750, 1800, 1890, 1946, 2000, 2016, 2025, 2085, 2100, 2160, 2224, 2240, 2250, 2268, 2400, 2502,
                    2520, 2592, 2625, 2700, 2780, 2800, 2835, 2880, 2919, 3000, 3024, 3150, 3240, 3336, 3360, 3375,
                    3475, 3500, 3600, 3753, 3780, 3892, 4000, 4032, 4050, 4170, 4200, 4320, 4448, 4500, 4536, 4725,
                    4800, 4865, 5004, 5040, 5184, 5250, 5400, 5560, 5600, 5670, 5838, 6000, 6048, 6255, 6300, 6480,
                    6672, 6720, 6750, 6950, 7000, 7200, 7506, 7560, 7784, 7875, 8000, 8100, 8340, 8400, 8640, 8757,
                    8896, 9000, 9072, 9450, 9730, 10008, 10080, 10125, 10425, 10500, 10800, 11120, 11200, 11259, 11340,
                    11676, 12000, 12096, 12510, 12600, 12960, 13344, 13500, 13900, 14000, 14175, 14400, 14595, 15012,
                    15120, 15568, 15750, 16200, 16680, 16800, 17375, 17514, 18000, 18144, 18765, 18900, 19460, 20016,
                    20160, 20250, 20850, 21000, 21600, 22240, 22518, 22680, 23352, 23625, 24000, 24325, 25020, 25200,
                    25920, 26271, 26688, 27000, 27800, 28000, 28350, 29190, 30024, 30240, 31136, 31275, 31500, 32400,
                    33360, 33600, 34750, 35028, 36000, 36288, 37530, 37800, 38920, 40032, 40500, 41700, 42000, 43200,
                    43785, 44480, 45036, 45360, 46704, 47250, 48650, 50040, 50400, 52125, 52542, 54000, 55600, 56000,
                    56295, 56700, 58380, 60048, 60480, 62272, 62550, 63000, 64800, 66720, 69500, 70056, 70875, 72000,
                    72975, 75060, 75600, 77840, 78813, 80064, 81000, 83400, 84000, 87570, 90072, 90720, 93408, 93825,
                    94500, 97300, 100080, 100800, 104250, 105084, 108000, 111200, 112590, 113400, 116760, 120096,
                    121625, 125100, 126000, 129600, 131355, 133440, 139000, 140112, 141750, 145950, 150120, 151200,
                    155680, 156375, 157626, 162000, 166800, 168000, 175140, 180144, 181440, 186816, 187650, 189000,
                    194600, 200160, 208500, 210168, 216000, 218925, 222400, 225180, 226800, 233520, 240192, 243250,
                    250200, 252000, 262710, 278000, 280224, 281475, 283500, 291900, 300240, 302400, 311360, 312750,
                    315252, 324000, 333600, 350280, 360288, 364875, 375300, 378000, 389200, 394065, 400320, 417000,
                    420336, 437850, 450360, 453600, 467040, 469125, 486500, 500400, 504000, 525420, 556000, 560448,
                    562950, 567000, 583800, 600480, 625500, 630504, 648000, 656775, 667200, 700560, 720576, 729750,
                    750600, 756000, 778400, 788130, 834000, 840672, 875700, 900720, 907200, 934080, 938250, 973000,
                    1000800, 1050840, 1094625, 1112000, 1125900, 1134000, 1167600, 1200960, 1251000, 1261008, 1313550,
                    1401120, 1407375, 1459500, 1501200, 1512000, 1556800, 1576260, 1668000, 1681344, 1751400, 1801440,
                    1876500, 1946000, 1970325, 2001600, 2101680, 2189250, 2251800, 2268000, 2335200, 2502000, 2522016,
                    2627100, 2802240, 2814750, 2919000, 3002400, 3152520, 3283875, 3336000, 3502800, 3602880, 3753000,
                    3892000, 3940650, 4203360, 4378500, 4503600, 4536000, 4670400, 5004000, 5044032, 5254200, 5629500,
                    5838000, 6004800, 6305040, 6567750, 7005600, 7506000, 7784000, 7881300, 8406720, 8757000, 9007200,
                    9851625, 10008000, 10508400, 11259000, 11676000, 12610080, 13135500, 14011200, 15012000, 15762600,
                    17514000, 18014400, 19703250, 21016800, 22518000, 23352000, 25220160, 26271000, 30024000, 31525200,
                    35028000, 39406500, 42033600, 45036000, 52542000, 63050400, 70056000, 78813000, 90072000, 105084000,
                    126100800, 157626000, 210168000, 315252000, 630504000}
        self.assertEqual(expected, result)

    def test_simple_divisors_count(self):
        arg = 24
        result = Modular.divisors_count(arg)
        expected = 8
        self.assertEqual(expected, result)

    def test_divisors_count_of_one(self):
        arg = 1
        result = Modular.divisors_count(arg)
        expected = 1
        self.assertEqual(expected, result)

    def test_divisors_count_of_two(self):
        arg = 2
        result = Modular.divisors_count(arg)
        expected = 2
        self.assertEqual(expected, result)

    def test_simple_divisors_count_large_numbers(self):
        arg = 630504000
        result = Modular.divisors_count(arg)
        expected = 560
        self.assertEqual(expected, result)

    def test_kanon(self):
        expected = {
            2: 5,
            3: 1
        }
        a = 96

        result = Modular.kanon(a)
        self.assertEqual(expected, result)

    def test_kanon2(self):
        expected = {
            2: 4,
            3: 1,
            5: 2
        }
        a = 1200

        result = Modular.kanon(a)
        self.assertEqual(expected, result)

    def test_pi1(self):
        expected = 0
        a = 1
        self.assertEquals(expected, Modular.pi(a))

    def test_pi2(self):
        expected = 1
        a = 2
        self.assertEquals(expected, Modular.pi(a))

    def test_pi3(self):
        expected = 2
        a = 3
        self.assertEquals(expected, Modular.pi(a))

    def test_pi4(self):
        expected = 7
        a = 20
        self.assertEquals(expected, Modular.pi(a))

    def test_pi4(self):
        expected = 7
        a = 19
        self.assertEquals(expected, Modular.pi(a))
