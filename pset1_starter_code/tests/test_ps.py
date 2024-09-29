import sys

sys.path.append('/home/james_mctighe/chem_274B/problem_sets/CHEM274B_PS1/pset1_starter_code/')

from reverse_linked_list import ListNode, Solution


def test_reverse_linked_list():
    # create a linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution
    # sol.print_list(self=sol,head=head)
    head = sol.reverse_linked_list(head)

    assert sol.print_list(head) == "5 4 3 2 1 "

