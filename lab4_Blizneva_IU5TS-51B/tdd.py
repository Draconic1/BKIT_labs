import unittest

from builder import *

class TestCost(unittest.TestCase):

    def test_cost(self):
        assert check_cost("ASUS 101") == 100000

if __name__ == "__main__":
    unittest.main()