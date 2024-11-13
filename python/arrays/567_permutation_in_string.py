class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # if len(s1) > len(s2):
        #     return False
        
        # s1Count = [0] * 26
        # s2Count = [0] * 26
        # matches = 0
        # for i in range(len(s1)):
        #     s1Count[ord(s1[i]) - ord('a')] += 1
        #     s2Count[ord(s2[i]) - ord('a')] += 1
        
        # for i in range(26):
        #     matches += 1 if s1Count[i] == s2Count[i] else 0

        # l = 0
        # for i in range(len(s1), len(s2)):
        #     if matches == 26 :
        #         return True
            
        #     index = ord(s2[i]) - ord('a')
        #     s2Count[index] += 1
        #     if s1Count[index] == s2Count[index]:
        #         matches += 1
        #     elif s1Count[index] + 1 == s2Count[index]:
        #         matches -= 1

        #     index = ord(s2[l]) - ord('a')
        #     s2Count[index] -= 1
        #     if s1Count[index] == s2Count[index]:
        #         matches += 1
        #     elif s1Count[index] - 1 == s2Count[index]:
        #         matches -= 1
        #     l += 1

        # return matches == 26

        if len(s1) > len(s2):
            return False

        char_count = [0] * 26

        for char in s1:
            char_count[ord(char) - ord('a')] += 1

        window = [0] * 26
        
        for i in range(len(s2)):
            window[ord(s2[i]) - ord('a')] += 1
            if i >= len(s1):
                window[ord(s2[i - len(s1)]) - ord('a')] -= 1
               
            if window == char_count:
                return True

        return False