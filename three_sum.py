from operator import itemgetter

class Solution:
    def three_sum(self, nums):

        sum_list = []
        sum_set = []

        n = len(nums)
        nums.sort()

        # iterates over elements, determines if valid, then adds to running list, quadratic
        for i in range(n -2):

            j = i + 1
            k = n - 1

            while j < k:
                proposed_entry = [nums[i],nums[j],nums[k]]
                if self.valid_entry(proposed_entry):
                    proposed_entry.sort()
                    sum_list.append(proposed_entry)
                    j += 1
                    k -= 1
                elif sum(proposed_entry) < 0:
                    j += 1
                else:
                    k -= 1

        #remove duplicate entries and return list, quadratic
        res = [i for n, i in enumerate(sum_list) if i not in sum_list[:n]]
        return res

    def valid_entry(self,nums): # determines if this matches the return criteria
        if self.not_equal(nums) and sum(nums) == 0:
            return True
        else:
            return False

    def not_equal(self, input_list): # determines if all elements are not equal to eachother
        i = input_list[0]
        j = input_list[1]
        k = input_list[2]

        if i != j and i != k and j !=k:
            return True
        else:
            return False

"""
TODO
sort the list of lists by the indicies
"""

test = Solution()

a = [0,1,-1,2,-2,2,-2]


y = test.three_sum(a)
print(y)