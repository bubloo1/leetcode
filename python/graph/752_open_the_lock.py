from typing import List
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        def keyConfig(key):
            res = []
            for i in range(4):
                digit = str((int(key[i]) + 1) % 10)
                res.append(key[:i] + digit + key[i+1:])
                digit = str((int(key[i]) + 10 - 1) % 10)
                res.append(key[:i] + digit + key[i+1:]) 
            return res


        queue = deque()
        queue.append(["0000",0])
        visited = set(deadends)

        while queue:
            key, turn = queue.popleft()

            if key == target:
                return turn
            
            for currKey in keyConfig(key):
                if currKey not in visited:
                    visited.add(currKey)
                    queue.append([currKey,turn+1])
        
        return -1


        