import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from reverse_linked_list import ListNode, Solution

class TestValidSymbols(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def list_to_array(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    # @weight(1)
    # @number("1.1")
    def test_empty_list(self):
        self.assertIsNone(self.solver.reverse_linked_list(None))

    # @weight(1)
    # @number("1.2")
    def test_single_node(self):
        head = ListNode(1)
        reversed_head = self.solver.reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), [1])

    # @weight(1)
    # @number("1.3")
    def test_two_nodes(self):
        head = ListNode(1, ListNode(2))
        reversed_head = self.solver.reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), [2, 1])

    # @weight(1)
    # @number("1.4")
    def test_multiple_nodes(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        reversed_head = self.solver.reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), [5, 4, 3, 2, 1])

    # @weight(1)
    # @number("1.5")
    def test_negative_values(self):
        head = ListNode(-1, ListNode(-2, ListNode(-3)))
        reversed_head = self.solver.reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), [-3, -2, -1])

    # @weight(1)
    # @number("1.6")
    def test_mixed_values(self):
        head = ListNode(1, ListNode(-2, ListNode(3, ListNode(-4))))
        reversed_head = self.solver.reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), [-4, 3, -2, 1])

    # @weight(1)
    # @number("1.7")
    def test_duplicate_values(self):
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(2))))
        reversed_head = self.solver.reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), [2, 2, 1, 1])

    # @weight(1)
    # @number("1.8")
    def test_large_list(self):
        head = ListNode(0)
        current = head
        for i in range(1, 1000):
            current.next = ListNode(i)
            current = current.next
        reversed_head = self.solver.reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), list(range(999, -1, -1)))

    # @weight(1)
    # @number("1.9")
    def test_all_same_values(self):
        head = ListNode(5, ListNode(5, ListNode(5, ListNode(5))))
        reversed_head = self.solver.reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), [5, 5, 5, 5])

    # @weight(1)
    # @number("1.10")
    def test_alternating_values(self):
        head = ListNode(1, ListNode(2, ListNode(1, ListNode(2))))
        reversed_head = self.solver.reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), [2, 1, 2, 1])