from typing import List
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        numsCount = {}
        for i in range(len(hand)):
            numsCount[hand[i]] = 1 + numsCount.get(hand[i], 0)

        minHeap =list(numsCount.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first,first + groupSize):
                if i not in numsCount:
                    return False
                numsCount[i] -= 1
                if  numsCount[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
                


newObject = Solution()
print(newObject.isNStraightHand([1,2,3,6,2,3,4,7,8],3))