class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenOfString = 0
        countOfLastWord = 0
        maxCountOfLastWord = 0
        s+=' '
        while lenOfString < len(s):
            if s[lenOfString] != " ":
                countOfLastWord += 1
            else:
                if(countOfLastWord > 0):
                    maxCountOfLastWord = countOfLastWord
                countOfLastWord = 0
            lenOfString += 1
        return maxCountOfLastWord
