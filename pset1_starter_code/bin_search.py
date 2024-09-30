import math

class Solution:
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:

            mid = low + (high - low) // 2
            # print(mid)

            if arr[mid] == target:
                return f"target is located at the {mid} index"
            
            elif arr[mid] < target:
                low = mid + 1
                print(f"low = {low}")

            else:
                high = mid - 1
                print(f"high = {high}")

        return f"Element {target} not present within list"


a = Solution()

b = [x for x in range(1010)]


print(a.binary_search(b,450))