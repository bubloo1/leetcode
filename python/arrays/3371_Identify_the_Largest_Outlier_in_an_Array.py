from typing import List
from collections import Counter
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # 2x + y = sum(nums)
        tot_sum = sum(nums)
        freq_map = Counter(nums)
        res = float('-inf')
        
        for num in nums:
            temp = tot_sum - num
            
            if temp % 2 != 0:
                continue
            
            val = temp // 2
            
            if val in freq_map and (val != num or freq_map[val] > 1):
                res = max(res, num)
        
        return res