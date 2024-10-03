class Queue:

    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        self.stack1.append(val)

    def dequeue(self):
        if not self.is_empty():
            # raise IndexError("Trying to dequeue an empty queue")
            return False
        
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            # raise ValueError("Empty Queue")
            return False
        else:
            return self.stack1[0]

    def is_empty(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True

    def get_size(self):
        # TODO: Implement
        pass



