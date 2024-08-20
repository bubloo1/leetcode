class Solution:
    def removeDuplicates(self, nums) -> int:

        right = left = 0
        lenOfNums = len(nums)

        while right + 1 < lenOfNums:
            count = 1
            while right + 1 < lenOfNums and nums[right] == nums[right+1]:
                count += 1
                right + 1
            
            for i in range(min(2, count)):
                nums[left] = nums[right]
                left += 1
            right += 1
        
        return left




newObject = Solution()

print(newObject.removeDuplicates([1,1,1,2,2,3]))