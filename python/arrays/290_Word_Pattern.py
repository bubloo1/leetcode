class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        charsToWords = {}
        wordsToChars = {}

        for c,w in zip(pattern, words):
            if c in charsToWords and charsToWords[c] != w:
                return False 
            if w in wordsToChars and wordsToChars[w] != c:
                return False 
            charsToWords[c] = w
            wordsToChars[w] = c
        return True
