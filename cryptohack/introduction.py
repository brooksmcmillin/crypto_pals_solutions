import base64
import Crypto
import unittest

# Introduction to Cryptohack Challenges
class TestIntro(unittest.TestCase):

    # Hex
    def test_hex(self):
        input_text = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
        text = bytes.fromhex(input_text)
        self.assertEqual(text, b'crypto{You_will_be_working_with_hex_strings_a_lot}')

    # Base64
    def test_base64(self):
        input_text = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
        text = bytes.fromhex(input_text)
        b64 = base64.b64encode(text)
        self.assertEqual(b64, b'crypto/Base+64+Encoding+is+Web+Safe/')

        
if __name__ == "__main__":
    unittest.main()

