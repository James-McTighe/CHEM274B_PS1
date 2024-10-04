import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from fib import Solution

class TestFib(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    # @weight(1)
    # @number("1.1")
    def test_fibonacci_empty(self):
        self.assertEqual(self.solver.fib_recursive(0), [])
        self.assertEqual(self.solver.fib_iterative(0), [])
    
    # @weight(1)
    # @number("1.2")
    def test_fibonacci_one(self):
        self.assertEqual(self.solver.fib_recursive(1), [0])
        self.assertEqual(self.solver.fib_iterative(1), [0])

    # @weight(1)
    # @number("1.3")
    def test_fibonacci_two(self):
        self.assertEqual(self.solver.fib_recursive(2), [0, 1])
        self.assertEqual(self.solver.fib_iterative(2), [0, 1])

    # @weight(1)
    # @number("1.4")
    def test_fibonacci_ten(self):
        self.assertEqual(self.solver.fib_recursive(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(self.solver.fib_iterative(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    # @weight(1)
    # @number("1.5")
    def test_fibonacci_twenty(self):
        self.assertEqual(self.solver.fib_iterative(20), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])

    # @weight(1)
    # @number("1.6")
    def test_fibonacci_negative(self):
        self.assertEqual(self.solver.fib_recursive(-5), [])
        self.assertEqual(self.solver.fib_iterative(-5), [])

    # @weight(1)
    # @number("1.7")
    def test_fibonacci_one_negative(self):
        self.assertEqual(self.solver.fib_recursive(-1), [])
        self.assertEqual(self.solver.fib_iterative(-1), [])
    
    # @weight(1)
    # @number("1.8")
    def test_fibonacci_iterative(self):
        self.assertTrue(self.solver.fib_iterative(35)[-1], 5702887)