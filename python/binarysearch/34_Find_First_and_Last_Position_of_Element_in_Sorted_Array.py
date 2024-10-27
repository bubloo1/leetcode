class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(nums,target,bias):
            low,high = 0, len(nums) - 1
            i = -1
            while low <= high:
                mid = (low + high)//2

                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    i = mid
                    if bias:
                        high = mid - 1
                    else:
                        low = mid + 1
            return i
        return [binarySearch(nums,target,True),binarySearch(nums,target,False)]