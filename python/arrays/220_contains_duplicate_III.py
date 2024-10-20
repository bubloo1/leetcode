
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        if valueDiff < 0:
            return False
        
        buckets = {}
        bucket_size = valueDiff + 1  # Bucket size should be t + 1 to account for zero difference

        for i, num in enumerate(nums):
            bucket_key = num // bucket_size
            print(bucket_key,"bucketKey")
            # Check if the current bucket already has a number
            if bucket_key in buckets:
                return True
            
            # Check the previous bucket
            if (bucket_key - 1 in buckets and 
                abs(num - buckets[bucket_key - 1]) < bucket_size):
                return True

            # Check the next bucket
            if (bucket_key + 1 in buckets and 
                abs(num - buckets[bucket_key + 1]) < bucket_size):
                return True

            # Insert the current number into the bucket
            buckets[bucket_key] = num

            # Remove numbers that are out of the k range
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // bucket_size]
        
        return False

        # for i in range(len(nums)):
        #     for j in range(i + 1,min(i + 1 + indexDiff, len(nums))):
        #         if abs(nums[i] - nums[j]) <= valueDiff:
        #             return True
        # return False 
        # for i in range(len(nums)):
        #     for j in range(i + 1,len(nums)):
        #         if abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff:
        #             return True
        # return False 
    

newObject = Solution()
print(newObject.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3))  

 