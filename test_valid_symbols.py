import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from valid_symbols import Solution

class TestValidSymbols(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    # @weight(1)
    # @number("2.1")
    def test_case_1(self):
        self.assertEqual(self.solver.valid_symbols("()"), True)
        
    # @weight(1)
    # @number("2.2")
    def test_case_2(self):
        self.assertEqual(self.solver.valid_symbols("()[]{}"), True)
        
    # @weight(1)
    # @number("2.3")
    def test_case_3(self):
        self.assertEqual(self.solver.valid_symbols("(]"), False)

    # @weight(1)
    # @number("2.4")
    def test_case_4(self):
        self.assertEqual(self.solver.valid_symbols(")"), False)
        
    # @weight(1)
    # @number("2.5")
    def test_case_5(self):
        self.assertEqual(self.solver.valid_symbols("((((("), False)

    # @weight(1)
    # @number("2.6")
    def test_case_6(self):
        self.assertEqual(self.solver.valid_symbols("()(){}[]{[]}"), True)

    # @weight(1)
    # @number("2.7")
    def test_case_7(self):
        self.assertEqual(self.solver.valid_symbols("({}[]{}[]{}{})"), True)

    # @weight(1)
    # @number("2.8")
    def test_case_8(self):
        self.assertEqual(self.solver.valid_symbols("}"), False)

    # @weight(2)
    # @number("2.9")
    def test_case_9(self):
        s = "".join(["{}" for i in range(10000)])
        self.assertEqual(self.solver.valid_symbols(s), True)