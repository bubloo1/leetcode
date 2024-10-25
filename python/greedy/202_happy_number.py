class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumSquareDigits(n)

            if n == 1:
                return True
        return False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output