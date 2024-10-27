class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        start,end = 0, k - 1
        ans = float('inf')
        while end < len(nums):
            diff = nums[end] - nums[start]
            ans = min(diff,ans)
            start += 1
            end += 1
        return ans



#    nums.sort()
#         l, r = 0, k - 1
#         res = float("inf")
        
#         while r < len(nums):
#             res = min(res, nums[r] - nums[l])
#             l, r = l + 1, r + 1
#         return res