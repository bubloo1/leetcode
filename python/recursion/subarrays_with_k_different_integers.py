class Solution:
    def subarraysWithKDistinct(self, nums, k: int):

        subarrays = []

        def backtrack(start, end):
           
            if end == len(nums):
                return

            elif start > end:
                backtrack(0, end + 1)
            else:
                subarrays.append(nums[start:end + 1])
            
                backtrack(start + 1, end)


        backtrack(0, 0)
        return subarrays


newObject = Solution()
print(newObject.subarraysWithKDistinct([1,2,3],2))
