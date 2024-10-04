import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from three_sum import Solution

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    # @weight(1)
    # @number("3.1")
    def test_three_sum_empty(self):
        self.assertEqual(self.solver.three_sum([]), [])

    # @weight(1)
    # @number("3.2")
    def test_three_sum_no_solution(self):
        self.assertEqual(self.solver.three_sum([1, 2, 3]), [])

    # @weight(1)
    # @number("3.3")
    def test_three_sum_one_solution(self):
        self.assertEqual(self.solver.three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    # @weight(1)
    # @number("3.4")
    def test_three_sum_multiple_solutions(self):
        self.assertEqual(self.solver.three_sum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])

    # @weight(1)
    # @number("3.5")
    def test_three_sum_duplicate_values(self):
        self.assertEqual(self.solver.three_sum([-1, 0, 1, 2, -1, -4, -1, 0, 1, 2, 2]), [[-4, 2, 2], [-1, -1, 2], [-1, 0, 1]])

    # @weight(1)
    # @number("3.6")
    def test_three_sum_negative_values(self):
        self.assertEqual(self.solver.three_sum([-4, -1, -1, 0, 1, 2]), [[-1, -1, 2], [-1, 0, 1]])

    # @weight(1)
    # @number("3.7")
    def test_three_sum_large_list(self):
        large_list = list(range(-1000, 1001))
        self.assertEqual(len(self.solver.three_sum(large_list)), 500000)

    # @weight(1)
    # @number("3.8")
    def test_three_sum_single_element(self):
        self.assertEqual(self.solver.three_sum([0]), [])

    # @weight(1)
    # @number("3.9")
    def test_three_sum_two_elements(self):
        self.assertEqual(self.solver.three_sum([0, 0]), [])

    # @weight(1)
    # @number("3.10")
    def test_three_sum_all_zeros(self):
        self.assertEqual(self.solver.three_sum([0, 0, 0]), [[0, 0, 0]])