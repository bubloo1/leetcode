class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        fact = 1
        numbers = []
        for i in range(1,n):
            fact *= i
            numbers.append(i)
        numbers.append(n)
        print(fact,"fact")
        ans = ""
        k -= 1

        while True:
            print(k//fact)
            ans += str(numbers[k//fact])
            numbers.pop(k//fact)
            if not numbers:
                break
            k %= fact
            fact //= len(numbers)

        return ans


newObject = Solution()
print(newObject.getPermutation(4,9))