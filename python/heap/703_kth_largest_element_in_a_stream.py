from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
    def add(self,num):
        heapq.heappush(self.minHeap,num)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]



newObject = KthLargest(3,[4,5,8,2])
print(newObject.add(3))
print(newObject.add(5))
print(newObject.add(10))
