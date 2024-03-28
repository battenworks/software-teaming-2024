import unittest


class TestFizzBuzz(unittest.TestCase):
    def test_1_returns_1(self):
        self.assertEqual(fizzbuzz(1), "1")
    

if __name__ == '__main__':
    unittest.main()
