from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        eachTaskCount = {}
        for i in range(len(tasks)):
            eachTaskCount[tasks[i]] = 1 + eachTaskCount.get(tasks[i], 0)
        
        maxHeap = [-count for count in eachTaskCount.values()]

        heapq.heapify(maxHeap)
        queue = []
        time = 0
        while maxHeap or queue:

            if not maxHeap:
                time = queue[0][1]
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    queue.append((count,time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap,queue.pop(0)[0])
            
            time += 1
        return time