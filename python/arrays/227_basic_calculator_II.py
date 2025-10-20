class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'  # Default sign before the first number
        s += '+'  # Add a '+' to handle the last number in the loop

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    prev = stack.pop()
                    # Truncate toward zero
                    stack.append(int(prev / num))
                sign = c
                num = 0
            elif c == ' ':
                continue  # Skip spaces

        return sum(stack)
                


sol = Solution()
print(sol.calculate("3+2*2"))