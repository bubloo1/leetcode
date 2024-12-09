from typing import List
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        # Calculate the minimum cost to shift each character in s to the corresponding character in t
        total_cost = 0
        n = len(s)

        for i in range(n):
            char_s = s[i]
            char_t = t[i]

            # Calculate the index of the characters in the alphabet
            index_s = ord(char_s) - ord('a')
            index_t = ord(char_t) - ord('a')
            print(index_s,index_t)
            # Calculate forward and backward distances
            forward_distance = (index_t - index_s) % 26
            backward_distance = (index_s - index_t) % 26
            
            # Calculate costs for forward and backward shifts
            forward_cost = 0
            backward_cost = 0

            for j in range(forward_distance):
                forward_cost += nextCost[(index_s + j) % 26]
            for j in range(backward_distance):
                backward_cost += previousCost[(index_s - j + 26) % 26]
         
            # Add the minimum cost to total_cost
            total_cost += min(forward_cost, backward_cost)

        return total_cost
    

newObect = Solution()
print(newObect.shiftDistance(s = "abab", t = "baba", 
                            nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                            previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))