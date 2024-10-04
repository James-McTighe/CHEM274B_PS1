import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from queue_linked_list import ListNode, Queue

class TestQueueUsingLinkedList(unittest.TestCase):
    # @weight(1)
    # @number("3.1")
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.get_size(), 1)

    # @weight(1)
    # @number("3.2")
    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.get_size(), 1)

    # @weight(1)
    # @number("3.3")
    def test_peek(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.get_size(), 2)

    # @weight(1)
    # @number("3.4")
    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

    # @weight(1)
    # @number("3.5")
    def test_get_size(self):
        queue = Queue()
        self.assertEqual(queue.get_size(), 0)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.get_size(), 2)

    # @weight(1)
    # @number("3.6")
    def test_dequeue_empty(self):
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.dequeue()

    # @weight(1)
    # @number("3.7")
    def test_peek_empty(self):
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.peek()

    # @weight(1)
    # @number("3.8")
    def test_multiple_operations(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(4)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.peek(), 3)
        self.assertEqual(queue.get_size(), 2)

    # @weight(1)
    # @number("3.9")
    def test_large_queue(self):
        queue = Queue()
        for i in range(1000):
            queue.enqueue(i)
        self.assertEqual(queue.get_size(), 1000)
        for i in range(1000):
            self.assertEqual(queue.dequeue(), i)
        self.assertTrue(queue.is_empty())

    # @weight(1)
    # @number("3.10")
    def test_alternating_enqueue_dequeue(self):
        queue = Queue()
        for i in range(100):
            queue.enqueue(i)
            self.assertEqual(queue.dequeue(), i)
        self.assertTrue(queue.is_empty())