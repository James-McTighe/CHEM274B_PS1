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

        # destination.append(value)
        destination.insert(0,value)
        ## TODO: implement collision resolution

    def get(self, key):
        return self.table[key]
    ## TODO: implement collision resolution

    def remove(self, key):
        self.table.remove(self._hash(key))
        ## TODO: implement collision resolution      

            
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
                    count += 1
        if self.count > self.size:
            self.resize()
        return self.count

    def insert(self, key, value):
        # TODO: Implement for 12.3
        pass

    def remove(self, key):
        # TODO: Implement for 12.3
        pass

    def resize(self):
        self.size *= 2
        new_table = [[] for _ in range(self.size)]
        # for x in self.table:



# Testing
