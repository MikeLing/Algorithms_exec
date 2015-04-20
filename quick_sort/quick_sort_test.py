import unittest
from quick_sort import *


class Testheapsort(unittest.TestCase):

    def setUp(self):
        self.ex = [2, 8, 7, 1, 3, 5, 6, 4]

    def test_quicksort(self):
        quick_sort(self.ex)
        self.assertEqual(self.ex,  [1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
