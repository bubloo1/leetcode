from typing import List
from collections import defaultdict
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numCount = defaultdict(list)

        for n in arr:
            numCount[n] = 1 + numCount.get(n,0)
        
        minHeap = []
        for val in numCount.values():
            heapq.heappush(minHeap,val)
        
        heapq.heapify(minHeap)
        res = len(minHeap)
        while k > 0 and minHeap:
            currPop = heapq.heappop(minHeap)
            if currPop <= k:
                k -= currPop
                res -= 1
        
        return res
        


newObject = Solution()
print(newObject.findLeastNumOfUniqueInts(arr = [2,4,1,8,3,5,1,3], k = 3))