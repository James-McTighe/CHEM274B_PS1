class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        converted_list = [ord(str(x)) for x in key]
        sum_total = sum(converted_list)

        return (sum_total * 31) % self.size

    def insert(self, key, value):
        destination = self.table[key]
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
        count = 0
        for _ in self.table:
            if not _:
                continue
            else:
                for x in _ :
                    count += 1

        return count

    def insert(self, key, value):
        # TODO: Implement for 12.3
        pass

    def remove(self, key):
        # TODO: Implement for 12.3
        pass

    def resize(self):
        # TODO: Implement for 12.3
        pass


# Testing
a = HashTable(10)
print(a.load_factor())
print(a.table)
b = []

a.insert(0,10)
a.insert(0,20)
a.insert(4,5)
print(a.table)

print(a.table)
print(a.load_factor())



