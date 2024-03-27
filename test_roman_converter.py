import unittest
from roman_converter import convert_to_roman


class TestRomanConverter(unittest.TestCase):
    def test_convert_number_1(self):
        self.assertEqual(convert_to_roman(1), 'I')

    def test_convert_number_2(self):
        self.assertEqual(convert_to_roman(2), 'II')

    def test_convert_number_3(self):
        self.assertEqual(convert_to_roman(3), 'III')

    def test_convert_number_4(self):
        self.assertEqual(convert_to_roman(4), 'IV')

    def test_convert_number_5(self):
        self.assertEqual(convert_to_roman(5), 'V')

    def test_convert_number_6(self):
        self.assertEqual(convert_to_roman(6), 'VI')

    def test_convert_number_9(self):
        self.assertEqual(convert_to_roman(9), 'IX')

    def test_convert_number_10(self):
        self.assertEqual(convert_to_roman(10), 'X')

    def test_convert_number_14(self):
        self.assertEqual(convert_to_roman(14), 'XIV')

    def test_convert_number_19(self):
        self.assertEqual(convert_to_roman(19), 'XIX')


if __name__ == '__main__':
    unittest.main()
