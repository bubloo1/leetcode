from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        ans = 0
        currentAns = 0
        while start < end:
            if height[start] < height[end]:
                currentAns = height[start] * (end - start)
                start += 1
            elif height[start] >= height[end]:
                currentAns = height[end] * (end - start)
                end -= 1
            ans = max(ans,currentAns)
        return ans