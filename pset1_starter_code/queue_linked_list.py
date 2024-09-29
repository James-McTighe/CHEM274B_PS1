class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, val):
        # TODO: Implement
        new_node = ListNode(val)

        if self.rear:
            self.rear.next = new_node
        self.rear = new_node

        if not self.front:
            self.front = new_node

        self.size += 1

    def dequeue(self):
        self.peek()
        
        dequeued_val = self.front.val
        self.front = self.front.next

        if not self.front:
            self.rear = None

        self.size -= 1
        return dequeued_val        

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.val

    def is_empty(self):
        
        return self.size == 0

    def get_size(self):
        return self.size
    
    