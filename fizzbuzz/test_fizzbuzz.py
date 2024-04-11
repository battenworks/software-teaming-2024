import unittest
import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_returns_1_for_1(self):
        self.assertEqual("1", fizzbuzz.fizzbuzz(1))

    def test_returns_fizz_for_3(self):
        self.assertEqual("fizz", fizzbuzz.fizzbuzz(3))

    def test_returns_buzz_for_5(self):
        self.assertEqual("buzz", fizzbuzz.fizzbuzz(5))

    def test_returns_fizzbuzz_for_15(self):
        self.assertEqual("fizzbuzz", fizzbuzz.fizzbuzz(15))


if __name__ == '__main__':
    unittest.main()
