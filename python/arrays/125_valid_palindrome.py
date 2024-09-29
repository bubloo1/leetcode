class Solution:
    def isPalindrome(self, s: str) -> bool:

        newString = ""

        for char in s:
            if char.isalpha() or char.isdigit():
                newString += char.lower()

        return newString == newString[::-1]


newObject = Solution()
print(newObject.isPalindrome("A man, a plan, a canal: Panama"))