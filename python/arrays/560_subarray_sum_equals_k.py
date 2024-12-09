class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        prefix_sum = {0:1}
       
        count = 0

        for n in nums:
            curr_sum = curr_sum + n
            diff = curr_sum - k
            count += prefix_sum.get(diff,0)
            prefix_sum[curr_sum] = 1 + prefix_sum.get(curr_sum,0)
        return count


        