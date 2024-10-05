class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        converted_list = [ord(str(x)) for x in key]
        sum_total = sum(converted_list)

        return (sum_total * 31) % self.size

    def insert(self, key, value):
        destination = self._hash(key)
        self.table[destination].append({key:value})
        
    def get(self, key):
        index = self._hash(key)
        query = self.table[index]

        if query:
            return self.table[index]
        else:
            return None
    

    def remove(self, key):
        self.table.remove(self._hash(key))
        
            
class DynamicHashTable(HashTable):
    def __init__(self, size):
        super().__init__(size)
        self.count = 0
        self.load_factor_threshold = 0.7

    def calculate_load_factor(self):
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
        self.table[destination].append({key:value})

        self.calculate_load_factor()

    def remove(self, key):
        self.table.remove(self._hash(key))


    def resize(self):
        old_table = self.table
        self.size *= 2
        new_table = [[] for _ in range(self.size)]
        for i in old_table:
            for key,value in i:
                self.insert(key,value)


# Testing
