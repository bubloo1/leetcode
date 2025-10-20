import heapq
from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []  # min-heap to track climbs

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue  # no resources needed if descending or equal

            heapq.heappush(heap, diff)

            # if we have more climbs than ladders, use bricks for the smallest one
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
                if bricks < 0:
                    return i  # can't reach the next building

        return len(heights) - 1  # reached the last building