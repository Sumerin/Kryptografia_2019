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
        expected = "SZYFR KWADRATOWY NAZYWANY JEST TAKŻE MACIERZOWYM"
        encrypted = "SFKZRWY ADTYRO AWNAWYZA YNJE KSTŻTAE CRMIZAEOWACYĄĆMBD"

        result = Cipher.matrix_cipher(encrypted, w=3)
        self.assertEquals(expected, result)

if __name__ == '__main__':
    unittest.main()
