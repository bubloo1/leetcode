from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqCount = {}

        for n in nums:
            freqCount[n] = 1 + freqCount.get(n,0)
        
        topKElements = []

        for val,freq in freqCount.items():
            heapq.heappush(topKElements,(freq,val))
            if len(topKElements) > k:
                heapq.heappop(topKElements)
        
        result = [ele for freq, ele in topKElements]

        return result


newObject = Solution()

print(newObject.topKFrequent([1,1,1,2,2,3], 2))