class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Reverse the input strings to start from the least significant digit
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        result = []
        carry = 0

        # Iterate through the digits of both numbers
        for i in range(max(len(num1),len(num2))):
            digit1 = int(num1[i]) if i < len(num1) else 0
            digit2 = int(num2[i]) if i < len(num2) else 0

            # Calculate the sum of the digits and the carry
            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(str(total % 10))

        # If there is a remaining carry, add it to the result
        if carry:
            result.append(str(carry))
        
        # Reverse the result string and return it
        return ''.join(result[::-1])

        