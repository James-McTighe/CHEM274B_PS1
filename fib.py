class Solution:
    def fib_recursive(self, n):
       
       def recursion_method(x):
            if x == 0:
                return 0
            if x == 1:
                return 1
            return recursion_method(x-1) + recursion_method(x-2)
        
    #    for x in range(n):
    #         print(recursion_method(x))
    
    def fib_iterative(self, n):
        a = 0
        b = 1

        for x in range(n):
            
            print(a)
            
            temp_a = a
            temp_b = b
            a = b
            b = temp_a + temp_b

        

if __name__ == "__main__":

    a = Solution()
    print("----------------")
    print("Iterative Method")
    print("----------------")
    print(a.fib_iterative(10))

    print("\n")
    print("----------------")
    print("Recursive Method")
    print("----------------")
    print(a.fib_recursive(10))
