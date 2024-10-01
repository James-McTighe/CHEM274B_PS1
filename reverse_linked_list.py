class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def print_list(head):
        output = ""
        while head is not None:
            output += str(head.val)
            output += " "
            head = head.next
        return output
    
    @staticmethod
    def reverse_linked_list(head):
        # TODO: Implement
        curr = head
        prev = None

        while curr is not None:
            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node

        return prev
    

if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # print("Given Linked list:", end="")
    print(Solution.print_list(head))

    head = Solution.reverse_linked_list(head)

    # print("Reversed Linked List:", end="")
    print(Solution.print_list(head))