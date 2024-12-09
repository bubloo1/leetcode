from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        combinedSum= []
        #we check min here because if k < len(nums2) we dont need iterate entire len(nums2)
        for i in range(min(k,len(nums2))):
            heapq.heappush(combinedSum,(nums1[0] + nums2[i], 0,i))
        
        res = []
        # we will only calculate until its len(res) < k  
        while combinedSum and len(res) < k:
            currSum,i,j = heapq.heappop(combinedSum)
            res.append([nums1[i],nums2[j]])

            if i + 1 < len(nums1):
                heapq.heappush(combinedSum,(nums1[i+1] + nums2[j],i+1,j))
        
        return res


newObject = Solution()
print(newObject.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 6))