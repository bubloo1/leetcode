class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        fact = 1
        numbers = []
        for i in range(1,n+1):
            fact *= i
            numbers.append(i)

        ans = ""
        k -= 1

        while True:
            ans += str(numbers[k//fact])
            numbers.pop(k//fact)
            if not numbers:
                break
            k %= fact
            fact //= len(numbers)

        return ans


newObject = Solution()
print(newObject.getPermutation(3,3))