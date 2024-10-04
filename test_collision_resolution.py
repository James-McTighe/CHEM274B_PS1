import unittest
import random
import string
# from gradescope_utils.autograder_utils.decorators import weight, number
from collision_resolution import SeparateChainingHashTable, LinearProbingHashTable

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

class TestCollisionHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = SeparateChainingHashTable(10)
        self.hash_table_lp = LinearProbingHashTable(10)

    # @weight(1)
    # @number("2.1")
    def test_insert_and_get(self):
        self.hash_table.insert("apple", 5)
        self.assertEqual(self.hash_table.get("apple"), 5)

    # @weight(1)
    # @number("2.2")
    def test_update_existing_key(self):
        self.hash_table.insert("banana", 2)
        self.hash_table.insert("banana", 3)
        self.assertEqual(self.hash_table.get("banana"), 3)
    
    # @weight(1)
    # @number("2.3")
    def test_remove(self):
        self.hash_table.insert("cherry", 7)
        self.hash_table.remove("cherry")
        self.assertIsNone(self.hash_table.get("cherry"))

    # @weight(1)
    # @number("2.4")
    def test_get_nonexistent_key(self):
        self.assertIsNone(self.hash_table.get("nonexistent"))

    # @weight(1)
    # @number("2.5")
    def test_insert_and_get_linear_probing(self):
        self.hash_table_lp.insert("apple", 5)
        self.assertEqual(self.hash_table_lp.get("apple"), 5)

    # @weight(1)
    # @number("2.6")
    def test_update_existing_key_linear_probing(self):
        self.hash_table_lp.insert("banana", 2)
        self.hash_table_lp.insert("banana", 3)
        self.assertEqual(self.hash_table_lp.get("banana"), 3)

    # @weight(1)
    # @number("2.7")
    def test_remove_linear_probing(self):
        self.hash_table_lp.insert("cherry", 7)
        self.hash_table_lp.remove("cherry")
        self.assertIsNone(self.hash_table_lp.get("cherry"))

    # @weight(1)
    # @number("2.8")
    def test_get_nonexistent_key_linear_probing(self):
        self.assertIsNone(self.hash_table_lp.get("nonexistent"))