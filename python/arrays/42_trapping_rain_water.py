from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:

        left,right = 0, len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        ans = 0
        while left < right:
            if maxRight < maxLeft:
                right -= 1
                maxRight = max(height[right],maxRight)
                ans = ans + maxRight - height[right]
            else:
                left += 1
                maxLeft = max(height[left],maxLeft)
                ans = ans + maxLeft - height[left]
        return ans

        