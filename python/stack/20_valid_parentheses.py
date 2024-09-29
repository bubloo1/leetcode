class Solution:
    def isValid(self, s: str) -> bool:
        allBrackets = {")":"(", "}":"{","]":"["}
        stack = []

        for char in s:
            if char not in allBrackets:
                stack.append(char)
                continue
            if not stack or stack[-1] != allBrackets[char]:
                return False
            stack.pop()
        return not stack





newObject = Solution()
print(newObject.isValid("()[]{}"))