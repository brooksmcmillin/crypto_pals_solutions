import unittest

from set1 import hex_to_base64, fixedXOR, xor_decode

class TestSet1(unittest.TestCase):

    def test_hex2base64(self):
        _input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        _output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(hex_to_base64(_input), _output)

    def test_fixedXOR(self):
        _input1 = "1c0111001f010100061a024b53535009181c"
        _input2 = "686974207468652062756c6c277320657965"
        _output = "746865206b696420646f6e277420706c6179"
        self.assertEqual(fixedXOR(_input1, _input2), _output)

    def test_xor_decode(self):
        _input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        _output = "Cooking MC's like a pound of bacon"
        self.assertEqual(xor_decode(_input)[0], _output)

if __name__ == "__main__":
    unittest.main()
