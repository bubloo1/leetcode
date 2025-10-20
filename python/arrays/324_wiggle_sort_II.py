class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        nums.sort()
        res = [0] * n
        left = (n + 1) // 2 - 1
        right = n - 1

        for i in range(n):
            if i % 2 == 0:
                res[i] = nums[left]
                left -= 1
            else:
                res[i] = nums[right]
                right -= 1

        nums[:] = res  # copy back to original list