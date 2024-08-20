from typing import List
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0

        maxHeap = []
        i, n = 0, len(stations)
        stops = 0
        maxDistance = startFuel

        while maxDistance < target:
            while i < n and stations[i][0] <= maxDistance:
                heapq.heappush(maxHeap, -stations[i][1])
                i += 1

            if not maxHeap:
                return -1

            maxDistance += -heapq.heappop(maxHeap)
            stops += 1

        return stops


newObject = Solution()

print(newObject.minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))