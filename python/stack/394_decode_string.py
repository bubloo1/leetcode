class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr
                stack.pop()

                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                
                stack.append(int(multiplier) * subStr)
            
        return "".join(stack)
    

newObject = Solution()
print(newObject.decodeString("3[a]2[bc]")) #"aaabcbc"