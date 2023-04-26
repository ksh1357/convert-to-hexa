import unittest
import random

from dec_to_hex import dec_to_hex


class TestDecimalToHex(unittest.TestCase):
    """
    다음과 같은 경우를 테스트
    최솟값, 최대값, 양수/음수(int, float), 잘못된 입력
    """
    def test_random_int(self):
        n = random.randint(-1000000, 1000000)
        hex_str = dec_to_hex(n)
        self.assertEqual(hex_str, "%#x"%n)
    def test_random_float(self):
        n = random.uniform(-1000000, 1000000)
        hex_str = dec_to_hex(n)
        self.assertEqual(hex_str, "%#x"%int(n))
    def test_random_str_int(self):
        n = random.randint(-1000000, 1000000)
        hex_str = dec_to_hex(str(n))
        self.assertEqual(hex_str, "%#x"%int(n))
    def test_random_str_float(self):
        n = random.uniform(-1000000, 1000000)
        hex_str = dec_to_hex(str(n))
        self.assertEqual(hex_str, "%#x"%int(n))
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            dec_to_hex("abc")

if __name__=="__main__":
    unittest.main()