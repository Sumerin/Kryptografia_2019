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

if __name__ == '__main__':
    unittest.main()
