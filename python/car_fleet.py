class Solution:
    def carFleet(self, target: int, position, speed):
        posAndSpeed = [[p,s] for p,s in zip(position,speed)]
        stack = []

        for p,s in sorted(posAndSpeed, reverse = True):
            
            timeToReachTarget = (target - p)//s
            stack.append((timeToReachTarget))

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


newObject = Solution()

print(newObject.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))