class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # length_nums = len(nums) - 1
        # if length_nums == 0:
        #     return length_nums
        # left = 0
        # peak = 0
        # while left <= length_nums:

        #     if left == 0:
             
        #         if nums[left] > nums[left + 1]:
        #             peak = left
        #     elif left == length_nums:
               
        #         if nums[left] > nums[left - 1]:
        #             peak = left
        #     else:
        #         if nums[left] > nums[left - 1] and nums[left] > nums[left + 1]:
        #             peak = left
        #     left += 1
        # return peak

        i=0
        j=len(nums)-1
        while(i<j):
            mid=(i+j)//2
            if(nums[mid]<nums[mid+1]):
                i=mid+1
            else:
                j=mid
        return i