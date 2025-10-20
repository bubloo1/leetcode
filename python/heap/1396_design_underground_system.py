class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {} # id -> (startStation, time)
        self.routeMap = {} # (start, end) -> [totalTime, count]

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checkInMap[id] = (startStation, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        startStation, time = self.checkInMap[id]
        route = (startStation, endStation)
        if route not in self.routeMap:
            self.routeMap[route] = [0, 0]
        self.routeMap[route][0] += t - time
        self.routeMap[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, count = self.routeMap[(startStation, endStation)]
        return totalTime / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)