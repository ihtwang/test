#coding=utf-8
import unittest
import number
class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_case(self):
        self.prime = number.is_prime(4)
        self.assertTrue(self.prime,msg="Is not prime!")
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()
