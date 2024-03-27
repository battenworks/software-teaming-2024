import unittest

class TestRomanConverter(unittest.TestCase):
    def test_convert_number_1(self):
        self.assertEqual(convert_to_roman(1), 'I')

if __name__ == '__main__':
    unittest.main()
