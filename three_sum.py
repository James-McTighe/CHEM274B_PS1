class Solution:
    def three_sum(self, nums):

        sum_set = {}

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if (i + j + k) == 0 and self.not_equal(i,j,k):
                        new_entry = [i,j,k]
                        new_entry.sort()
                        sum_set.update(new_entry)

        return sum_set

    def get_trips(self,nums):
        pass

    def not_equal(self, i, j, k):
        if i != j and i != k and j !=k:
            return True
        else:
            return False

"""
TODO
1. create a function to get sum values
    a. sort i <= j <= k
    b. those functions will get passed into a set
    c. return set
2. create a function to sort values
    a. call first function
    b. convert set to list
    c. sort by [0] then [1] then [2]
"""

# opening test data
file = open("threesum_test_data.txt", "r")

lines = [int(x) for x in file.readlines()]

test = Solution()

a = [-5,2,3]

print(test.three_sum(a))
