from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        def dfs(index, sequence):
            if index >= len(nums):
                print("seq",sequence)
                return
            
            sequence.append(nums[index])
            dfs(index+1, sequence)
            sequence.pop()
            dfs(index+1,sequence)

            return
            
        return dfs(0,[])


sol = Solution()
print(sol.maximumLength([1,2,3,4,5], 2))