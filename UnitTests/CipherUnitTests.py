import unittest
import Krypto.Cipher as Cipher


class CipherMethods(unittest.TestCase):

    def test_rail_fence_encipher_h3(self):
        expected = "SROWN   TŻOZF ŁTOYZAYBŁJŻWSAOYNŚIYPK NYU RTC"

        message = "SZYFR PŁOTKOWY ZNANY BYŁ JUŻ W STAROŻYTNOŚCI"

        result = Cipher.railFence_encipher(message, h=3)
        self.assertEquals(expected, result)

    def test_rail_fence_decipher_h3(self):
        expected = "SZYFR PŁOTKOWY ZNANY BYŁ JUŻ W STAROŻYTNOŚCI"
        encrypted = "SROWN   TŻOZF ŁTOYZAYBŁJŻWSAOYNŚIYPK NYU RTC"

        result = Cipher.railFence_decipher(encrypted, h=3)
        self.assertEquals(expected, result)

    def test_rail_fence_encipher_h4(self):
        expected = "KGRORAYTAIPF"

        message = "KRYPTOGRAFIA"

        result = Cipher.railFence_encipher(message, h=4)
        self.assertEquals(expected, result)

    def test_rail_fence_decipher_h4(self):
        expected = "KRYPTOGRAFIA"
        encrypted = "KGRORAYTAIPF"

        result = Cipher.railFence_decipher(encrypted, h=4)
        self.assertEquals(expected, result)

    def test_matrix_encipher_w3(self):
        expected = "SFKZRWY ADTYRO AWNAWYZA YNJE KSTŻTAE CRMIZAEOW==Y==M=="

        message = "SZYFR KWADRATOWY NAZYWANY JEST TAKŻE MACIERZOWYM"

        result = Cipher.matrix_cipher(message, w=3)
        self.assertEquals(expected, result)

    def test_matrix_decipher_w3(self):
        expected = "SZYFR KWADRATOWY NAZYWANY JEST TAKŻE MACIERZOWYMAĄBCĆD"
        encrypted = "SFKZRWY ADTYRO AWNAWYZA YNJE KSTŻTAE CRMIZAEOWACYĄĆMBD"

        result = Cipher.matrix_cipher(encrypted, w=3)
        self.assertEquals(expected, result)

    def test_column_encipher(self):
        expected = "RROAFGAPYEB ZWZMSOCY NIZMMLSEU WRLTRTOSEEKEIM JPAU "
        message = "PIERWSZYM PARAMETREM SZYFRU KOLUMNOWEGO JEST LICZBA"
        key = "JIHGFĘEDĆCBĄA"

        result = Cipher.column_encipher(message, key)
        self.assertEquals(expected, result)

    def test_column_encipher_pi_n(self):
        expected = "RROAFGAPYEB ZWZMSOCY NIZMMLSEU WRLTRTOSEEKEIM JPAU "
        message = "PIERWSZYM PARAMETREM SZYFRU KOLUMNOWEGO JEST LICZBA"
        pi = {
            0: 12,
            1: 11,
            2: 10,
            3: 9,
            4: 8,
            5: 7,
            6: 6,
            7: 5,
            8: 4,
            9: 3,
            10: 2,
            11: 1,
            12: 0,
        }
        n = 13

        result = Cipher.column_encipher_pi_n(message, pi, n)
        self.assertEquals(expected, result)

    def test_column_encipher2(self):
        expected = "SIEIRDDNRMHMUGAAMTMES"
        message = "AMIDSUMMERNIGHTSDREAM"
        key = "SWINDON"

        result = Cipher.column_encipher(message, key)
        self.assertEquals(expected, result)

    def test_column_decipher(self):
        expected = "PIERWSZYM PARAMETREM SZYFRU KOLUMNOWEGO JEST LICZBA"
        encrypted = "RROAFGAPYEB ZWZMSOCY NIZMMLSEU WRLTRTOSEEKEIM JPAU "
        key = "JIHGFĘEDĆCBĄA"

        result = Cipher.column_decipher(encrypted, key)
        self.assertEquals(expected, result)

    def test_column_decipher2(self):
        expected = "AMIDSUMMERNIGHTSDREAM"
        encrypted = "SIEIRDDNRMHMUGAAMTMES"
        key = "SWINDON"

        result = Cipher.column_decipher(encrypted, key)
        self.assertEquals(expected, result)

    def test_cesar_encipher(self):
        expected = "TŻŹHŚ DFŻBŚB LFTV RŚŻŹŁNBĘFŃ TŻŹHŚW RŚŻFTWYBLCDFIP"
        message = "SZYFR CEZARA JEST PRZYKŁADEM SZYFRU PRZESUWAJĄCEGO"
        key = 2

        result = Cipher.cesar(message, key)
        self.assertEquals(expected, result)

    def test_cesar_decipher(self):
        expected = "SZYFR CEZARA JEST PRZYKŁADEM SZYFRU PRZESUWAJĄCEGO"
        encrypted = "TŻŹHŚ DFŻBŚB LFTV RŚŻŹŁNBĘFŃ TŻŹHŚW RŚŻFTWYBLCDFIP"
        key = 2

        result = Cipher.cesar(encrypted, -key)
        self.assertEquals(expected, result)

    def test_vigenere_encipher(self):
        expected = "TĘO SŹŹFS LEŚV PÓĘOCOY EP SŹŹFSW Z LPDĘŃ JĘĘNÓŚAŹPWZŃ"
        message = "TEN SZYFR JEST PODOBNY DO SZYFRU Z KODEM JEDNORAZOWYM"
        key = "AĄB"
        m = len(key)

        result = Cipher.vigenere_encipher(message, key, m)
        self.assertEquals(expected, result)

    def test_vigenere_decipher(self):
        expected = "TEN SZYFR JEST PODOBNY DO SZYFRU Z KODEM JEDNORAZOWYM"
        encrypted = "TĘO SŹŹFS LEŚV PÓĘOCOY EP SŹŹFSW Z LPDĘŃ JĘĘNÓŚAŹPWZŃ"
        key = "AĄB"
        m = len(key)

        result = Cipher.vigenere_decipher(encrypted, key, m)
        self.assertEquals(expected, result)

if __name__ == '__main__':
    unittest.main()
