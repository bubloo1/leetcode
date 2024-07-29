class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        ans = 0
        maxRightHeight = height[right]
        maxLeftHeight = height[left]

        while left < right:
            if maxLeftHeight < maxRightHeight:
                left += 1
                maxLeftHeight = max(maxLeftHeight,height[left])
                ans = ans + maxLeftHeight - height[left]
            else:
                right -= 1
                maxRightHeight = max(maxRightHeight,height[right])
                ans = ans + maxRightHeight - height[right]
        return ans


newObject = Solution()

print(newObject.trap([0,1,0,2,1,0,1,3,2,1,2,1]))