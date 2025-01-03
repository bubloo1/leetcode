from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index,height = stack.pop()
                maxArea = max(maxArea,(i - index) * height)
                start = index
            stack.append((start,heights[i]))


        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea