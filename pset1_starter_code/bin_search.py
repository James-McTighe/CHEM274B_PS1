import math

class Solution:
    def binary_search(self, arr, target):
        low = arr[0]
        high = arr[-1]

        print(low)
        print(high)

        # while low <= high:

        #     mid = low + high // 2
        #     print(mid)

        #     if arr[mid] == target:
        #         return mid
            
        #     elif arr[mid] < target:
        #         low = mid + 1

        #     else:
        #         high = mid - 1

        return f"Element {target} not present within list"


a = Solution()

b = [x for x in range(101)]

print(b[45])

a.binary_search(b,45)