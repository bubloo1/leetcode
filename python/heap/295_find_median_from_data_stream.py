import heapq

class MedianFinder:
    def __init__(self):
        self.small,self.large = [],[]
        self.smallListLen,self.largeListLen = 0,0

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            self.largeListLen += 1
            heapq.heappush(self.large,num)
        else:
            self.smallListLen += 1
            heapq.heappush(self.small, -num)
        
        if self.smallListLen > self.largeListLen + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large,-val)

            self.smallListLen -= 1
            self.largeListLen += 1

        if self.largeListLen > self.smallListLen + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-val)

            self.smallListLen += 1
            self.largeListLen -= 1
        

    def findMedian(self) -> float:
        if self.smallListLen > self.largeListLen:
            return -self.small[0]
        elif self.largeListLen > self.smallListLen:
            return self.large[0]
        return (-1 * self.small[0] + self.large[0])/ 2.0

        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)

# obj.addNum(3)
# obj.addNum(4)
# print(obj.numsList)
print(obj.findMedian())
# print((obj.numsListLen//2))

