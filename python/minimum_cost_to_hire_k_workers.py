from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        res = float("inf")
        pairs = []

        for i in range(len(quality)):
            pairs.append((wage[i]/quality[i],quality[i]))
        
        pairs.sort()
        maxHeap = []
        total_quality = 0

        for rate, q in pairs:
            heapq.heappush(maxHeap,-q)
            total_quality += q

            if len(maxHeap) > k:
                total_quality += heapq.heappop(maxHeap)
            
            if len(maxHeap) == k:
                res = min(res,total_quality * rate)
        
        return res
        

newObject = Solution()
print(newObject.mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2))