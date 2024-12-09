from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        counterOfWord1, counterOfWord2 = {},{}

        for i in range(len(word1)):
            counterOfWord1[word1[i]] = 1 + counterOfWord1.get(word1[i],0)
            counterOfWord2[word2[i]] = 1 + counterOfWord2.get(word2[i],0)
        
        if set(counterOfWord1.keys()) != set(counterOfWord2.keys()):
            return False
        if sorted(counterOfWord1.values()) != sorted(counterOfWord2.values()):
            return False
        return True

newObject = Solution()
print(newObject.closeStrings("cabbba", "aabbss"))