import time
import random
import string

class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        self.load_factor_threshold = 0.7

    def _hash(self, key):
        converted_list = [ord(str(x)) for x in key]
        sum_total = sum(converted_list)

        return (sum_total * 31) % self.size

    def calculate_load_factor(self):
        self.count = 0
        for _ in self.table:
            if not _:
                continue
            else:
                for x in _ :
                    self.count += 1
        if self.count > (self.size * self.load_factor_threshold):
            self.resize()
        return self.count

    def insert(self, key, value):
        destination = self._hash(key)
        self.table[destination].append(value)

        self.calculate_load_factor()

    def remove(self, key):
        self.table.remove(self._hash(key))

    def get(self, key):
        index = self._hash(key)
        query = self.table[index]

        if query:
            return self.table[index]
        else:
            return None

    def resize(self):
        self.size *= 2
        new_table = [[] for _ in range(self.size)]
        for i in self.table:
           for key, value in i:
               self.insert(key, value)

class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def _hash(self, key):
        converted_list = [ord(str(x)) for x in key]
        sum_total = sum(converted_list)

        return (sum_total * 31) % self.size

    def insert(self, key, value):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = self._hash(index + 1)

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._hash(index + 1)

        return None

    def remove(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = None
                return
            index = self._hash(index + 1)

        return None

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def compare_performance():
    separate_chaining = SeparateChainingHashTable(10000)
    linear_probing = LinearProbingHashTable(10000)
    test_data = [(generate_random_string(10), i) for i in range(10000)]

    # Insert performance
    sc_insert_start = time.time()
    for key, value in test_data:
        separate_chaining.insert(key, value)
    sc_insert_end = time.time()

    lp_insert_start = time.time()
    for key, value in test_data:
        linear_probing.insert(key, value)
    lp_insert_end = time.time()

    print(f"Separate Chaining insert time: {sc_insert_end - sc_insert_start}")
    print(f"Linear Probing insert time: {lp_insert_end - lp_insert_start}")

    # Lookup performance
    sc_lookup_start = time.time()
    for _ in range(1000):
        key, _ = random.choice(test_data)
        separate_chaining.get(key)
    sc_lookup_end = time.time()

    lp_lookup_start = time.time()
    for _ in range(1000):
        key, _ = random.choice(test_data)
        linear_probing.get(key)
    lp_lookup_end = time.time()

    print(f"Separate Chaining lookup time: {sc_lookup_end - sc_lookup_start}")
    print(f"Linear Probing lookup time: {lp_lookup_end - lp_lookup_start}")

    # Remove performance
    sc_remove_start = time.time()
    for _ in range(1000):
        key, _ = random.choice(test_data)
        separate_chaining.remove(key)
    sc_remove_end = time.time()

    lp_remove_start = time.time()
    for _ in range(1000):
        key, _ = random.choice(test_data)
        linear_probing.remove(key)
    lp_remove_end = time.time()

    print(f"Separate Chaining remove time: {sc_remove_end - sc_remove_start}")
    print(f"Linear Probing remove time: {lp_remove_end - lp_remove_start}")

if __name__ == "__main__":
    compare_performance()