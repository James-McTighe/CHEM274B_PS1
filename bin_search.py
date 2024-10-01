class Solution:
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:

            mid = low + (high - low) // 2
            # print(mid)

            if arr[mid] == target:
                return mid
            
            elif arr[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return f"Element {target} not present within list"
