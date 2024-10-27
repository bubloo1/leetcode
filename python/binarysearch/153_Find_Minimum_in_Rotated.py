class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # low,high = 0,len(nums) - 1
        # mini_number = float('inf')

        # while low  < high:
        #     mid = (low + high)//2
        #     mini_number = min(mini_number,nums[mid])
        #     if nums[mid] > nums[high]:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return min(mini_number, nums[low])

        left, right = 0, len(nums) - 1

        while left < right:

            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

