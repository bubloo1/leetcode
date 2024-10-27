class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                if stack and stack[-1] != '*':
                    stack.pop()
            else:
                stack.append(char)

        return "".join(stack) if stack else ""



newObject = Solution()

print(newObject.removeStars("erase*****"))