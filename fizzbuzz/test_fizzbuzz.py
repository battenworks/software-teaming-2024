import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_returns_1_for_1(self):
        self.assertEqual("1", fizzbuzz.fizzbuzz(1))
    

if __name__ == '__main__':
    unittest.main()
