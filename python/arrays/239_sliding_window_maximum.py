from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  
        l = r = 0
        
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

        # brute force
        # res = []
        # for i in range(len(nums) - k):
        #     currMaxValue = float('-inf')
        #     for j in range(i,min(i + k,len(nums))):
        #         currMaxValue = max(currMaxValue,nums[j])
        #     res.append(currMaxValue)
        # return res
    

newObject = Solution()
print(newObject.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
