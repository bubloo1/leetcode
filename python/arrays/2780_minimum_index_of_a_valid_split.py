class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dominent = None
        count = 0
        for num in nums:
            if count == 0:
                dominent = num
            count += (1 if num == dominent else -1)
        
        totalCount = nums.count(dominent)
        if totalCount <= len(nums) // 2:
            return -1

        leftCount = 0 
        for i, num in enumerate(nums):
            if num == dominent:
                leftCount += 1
            if leftCount > (i + 1) // 2 and ((totalCount - leftCount) > (len(nums) - i - 1) // 2):
                return i
        return -1