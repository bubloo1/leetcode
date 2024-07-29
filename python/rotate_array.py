class Solution:
    def rotate(self, nums, k: int):
        def helper(l, r):
            while l < r:
                nums[l],nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        k = k % len(nums)

        helper(0, len(nums)-1)
        helper(0, k - 1)
        helper(k, len(nums)-1)

newObject = Solution()
print(newObject.rotate([1,2,3,4,5,6,7], k = 3))

