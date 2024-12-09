from typing import List
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfitHeap = []
        minCapitalHeap = [(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(minCapitalHeap)

        for i in range(k):
            while minCapitalHeap and minCapitalHeap[0][0] <= w:
                c,p = heapq.heappop(minCapitalHeap)
                heapq.heappush(maxProfitHeap,-p)
            if not maxProfitHeap:
                break
            w += -1 * heapq.heappop(maxProfitHeap)    

        return w   


newObject = Solution()
print(newObject.findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]))