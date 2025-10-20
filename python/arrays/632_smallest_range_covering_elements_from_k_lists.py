from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        left = right = nums[0][0]
        minHeap = []
        for i in range(k):
            l = nums[i]
            left = min(left, l[0])
            right = max(right,l[0])
            heapq.heappush(minHeap, (l[0], i, 0))
        
        res = [left, right]
        while True:
            n, i, idx = heapq.heappop(minHeap)
            idx += 1
            if idx == len(nums[i]):
                return res
            
            nextVal = nums[i][idx]
            heapq.heappush(minHeap,(nextVal, i, idx))
            right = max(right, nextVal)
            left = minHeap[0][0]
            if right - left < res[1] - res[0]:
                res = [left, right]

newObject = Solution()
print(newObject.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))