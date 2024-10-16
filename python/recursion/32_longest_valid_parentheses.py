class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
        # def findMaxValid(i: int, open_count: int, max_len: int) -> int:
        #     # Base case: If we reach the end of the string
        #     if i == len(s):
        #         return max_len
            
        #     if open_count < 0:
        #         # If open_count becomes negative, no valid substring possible from here
        #         return max_len
            
        #     if s[i] == '(':
        #         # If current char is '(', we increase the open count and recurse
        #         return max(
        #             findMaxValid(i + 1, open_count + 1, max_len), # Move forward considering this '('
        #             max_len
        #         )
        #     else:
        #         # If current char is ')', we try to close a valid '(' if possible
        #         if open_count > 0:
        #             # There is an open '(', so this forms a valid pair
        #             return max(
        #                 findMaxValid(i + 1, open_count - 1, max_len + 2), # Pair formed, increase valid length
        #                 max_len
        #             )
        #         else:
        #             # No open '(' to pair with, just move forward
        #             return findMaxValid(i + 1, open_count, max_len)
    
        # # Call the recursive function starting from index 0
        # return findMaxValid(0, 0, 0)



newObject = Solution()
print(newObject.longestValidParentheses(")()())"))