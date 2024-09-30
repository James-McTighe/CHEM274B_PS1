class Solution:
    def fib_recursive(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        print(n)
        return self.fib_recursive(n-1) + self.fib_recursive(n-2)
        


    def fib_iterative(self, n):
        # TODO: Implement
        pass

if __name__ == "__main__":

    a = Solution()
    print(a.fib_recursive(5))