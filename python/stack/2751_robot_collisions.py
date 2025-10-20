from typing import List
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        sortedRobots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []

        for pos, health, dir, idx in sortedRobots:
            if dir == "R":
                stack.append([pos, health, dir, idx])
            else:
                while stack and stack[-1][2] == "R" and health > 0:
                    if stack[-1][1] < health:
                        # Left wins
                        health -= 1
                        stack.pop()
                    elif stack[-1][1] > health:
                        # Right wins
                        stack[-1][1] -= 1
                        health = 0
                    else:
                        # Equal → both destroyed
                        stack.pop()
                        health = 0
                if health > 0:
                    stack.append([pos, health, dir, idx])
        stack.sort(key=lambda x: x[3])
        return [h for _, h, _, _ in stack]

newObject = Solution()
print(newObject.survivedRobotsHealths(positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"))