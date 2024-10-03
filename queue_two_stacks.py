class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:

    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        self.stack1.append(val)

    def dequeue(self):
        if not self.is_empty():
            raise IndexError
            # return 1
        
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            # raise ValueError("Empty Queue")
            return 1
        else:
            return self.stack1[0]

    def is_empty(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True

    def get_size(self):
        # TODO: Implement
        pass



