import unittest
from heap_sort import *


class Testheapsort(unittest.TestCase):

    def setUp(self):
        self.ex = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

    def test_build_max_heap(self):
        heap = build_max_heap(self.ex)
        self.assertEqual(heap, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_heap_sort(self):
        heap = heap_sort(self.ex)
        self.assertEqual(heap, [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])


if __name__ == '__main__':
    unittest.main()
