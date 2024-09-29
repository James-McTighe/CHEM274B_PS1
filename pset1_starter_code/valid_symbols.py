class Solution:
    def valid_symbols(self, s: str) -> bool:
        # TODO: Implement
        bracket_pairs = {'(':')','{':'}','[':']'}
        stack = []

        for char in s:

            if char in bracket_pairs.values():

                first_element = stack.pop()

                if bracket_pairs[first_element] != char:
                    return False
                
            else:
                stack.append(char)

            print(f"Current Stack: {stack}")

        return not stack
    

if __name__ == '__main__':
    a = Solution

    print(a.valid_symbols(a,'(([]]))'))
    
