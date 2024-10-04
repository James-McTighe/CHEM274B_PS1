import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from bin_search import Solution

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    # @weight(1)
    # @number("2.1")
    def test_binary_search_found(self):
        self.assertEqual(self.solver.binary_search([1, 3, 5, 7, 9], 5), 2)

    # @weight(1)
    # @number("2.2")
    def test_binary_search_not_found(self):
        self.assertEqual(self.solver.binary_search([1, 3, 5, 7, 9], 6), -1)

    # @weight(1)
    # @number("2.3")
    def test_binary_search_empty_list(self):
        self.assertEqual(self.solver.binary_search([], 5), -1)

    # @weight(1)
    # @number("2.4")
    def test_binary_search_single_element(self):
        self.assertEqual(self.solver.binary_search([42], 42), 0)
        self.assertEqual(self.solver.binary_search([42], 43), -1)

    # @weight(1)
    # @number("2.5")
    def test_binary_search_duplicate_values(self):
        self.assertTrue(self.solver.binary_search([1, 1, 3, 5, 7, 9, 9], 1) in set([0, 1]))
        self.assertTrue(self.solver.binary_search([1, 1, 3, 5, 7, 9, 9], 9) in set([5, 6]))
        self.assertEqual(self.solver.binary_search([1, 1, 3, 5, 7, 9, 9], 4), -1)

    # @weight(1)
    # @number("2.6")
    def test_binary_search_negative_values(self):
        self.assertEqual(self.solver.binary_search([-10, -5, 0, 5, 10], -5), 1)
        self.assertEqual(self.solver.binary_search([-10, -5, 0, 5, 10], 11), -1)

    # @weight(1)
    # @number("2.7")
    def test_binary_search_large_list(self):
        large_list = list(range(1, 10001))
        self.assertEqual(self.solver.binary_search(large_list, 5000), 4999)
        self.assertEqual(self.solver.binary_search(large_list, 0), -1)
        self.assertEqual(self.solver.binary_search(large_list, 10000), 9999)

    # @weight(1)
    # @number("2.8")
    def test_binary_search_repeated_values(self):
        self.assertTrue(self.solver.binary_search([1, 1, 1, 1, 1], 1) in range(5))
        self.assertEqual(self.solver.binary_search([1, 1, 1, 1, 1], 2), -1)