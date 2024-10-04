import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from hash_table import DynamicHashTable, HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.simple_hash_table = HashTable(1000)
        self.hash_table = HashTable(10)
        self.dynamic_hash_table = DynamicHashTable(10)

    # @weight(1)
    # @number("1.1")
    def test_simple_hash(self):
        self.assertEqual(self.simple_hash_table._hash("apple"), 430)
        self.assertEqual(self.simple_hash_table._hash("banana"), 879)
        self.assertEqual(self.simple_hash_table._hash("cherry"), 243)

    # @weight(1)
    # @number("1.2")  
    def test_different_strings_different_hashes(self):
        hash1 = self.simple_hash_table._hash("hello")
        hash2 = self.simple_hash_table._hash("world")
        self.assertNotEqual(hash1, hash2)

    # @weight(1)
    # @number("1.3")
    def test_insert_and_get(self):
        self.hash_table.insert("apple", 5)
        self.assertEqual(self.hash_table.get("apple"), 5)
        
    # @weight(1)
    # @number("1.4")
    def test_update_existing_key(self):
        self.hash_table.insert("banana", 2)
        self.hash_table.insert("banana", 3)
        self.assertEqual(self.hash_table.get("banana"), 3)
     
    # @weight(1)
    # @number("1.5")   
    def test_remove(self):
        self.hash_table.insert("cherry", 7)
        self.hash_table.remove("cherry")
        self.assertIsNone(self.hash_table.get("cherry"))
 
    # @weight(1)
    # @number("1.6")       
    def test_get_nonexistent_key(self):
        self.assertIsNone(self.hash_table.get("nonexistent"))

    # @weight(1)
    # @number("1.7")
    def test_load_factor(self):
        for i in range(7):
            self.dynamic_hash_table.insert(f"key{i}", i)
        self.assertAlmostEqual(self.dynamic_hash_table.calculate_load_factor(), 0.7, delta=0.01)

    # @weight(1)
    # @number("1.8")
    def test_resize(self):
        initial_size = len(self.dynamic_hash_table.table)
        for i in range(8):  # Insert enough items to trigger resize
            self.dynamic_hash_table.insert(f"key{i}", i)
        self.assertTrue(len(self.dynamic_hash_table.table) > initial_size)

    # @weight(1)
    # @number("1.9")
    def test_functionality_after_resize(self):
        for i in range(20):  # Insert enough items to trigger resize
            self.dynamic_hash_table.insert(f"key{i}", i)
        for i in range(20):
            self.assertEqual(self.dynamic_hash_table.get(f"key{i}"), i)