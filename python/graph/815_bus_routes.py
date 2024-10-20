from typing import List
from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stopToRoutes = defaultdict(set)

        for routeId,stops in enumerate(routes):
            for stop in stops:
                stopToRoutes[stop].add(routeId)

        print(stopToRoutes)

        queue = deque([(source, 0)])
        visitedStop = set([source])
        visitedRoutes = set()

        while queue:
            currentStop, busesTaken = queue.popleft()

            for routeId in stopToRoutes[currentStop]:
                if routeId in visitedRoutes:
                    continue
                visitedRoutes.add(routeId)

                for stop in routes[routeId]:
                    if stop == target:
                        return busesTaken + 1
                    if stop not in visitedStop:
                        visitedStop.add(stop)
                        queue.append((stop,busesTaken + 1))
        return -1

newObject = Solution()
print(newObject.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))
        
