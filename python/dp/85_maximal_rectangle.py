class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def calAreaOfRec(heights):
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

        rows,cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            area = calAreaOfRec(heights)
            maxArea = max(maxArea,area)
        return maxArea
    