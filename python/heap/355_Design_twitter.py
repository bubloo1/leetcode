from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
      self.tweetCount = 0
      self.tweetMap = defaultdict(list)
      self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
       self.tweetMap[userId].append((self.tweetCount, tweetId))
       self.tweetCount += 1
      

    def getNewsFeed(self, userId: int) -> List[int]:
    
        feed = self.tweetMap[userId][:]

        for followee in self.followMap[userId]:
            feed.extend(self.tweetMap[followee])
       
        feed.sort(key=lambda x: -x[0]) 
        return [tweetId for _, tweetId in feed[:10]]
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
       

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# class Twitter:
#     def __init__(self):
#         self.count = 0
#         self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
#         self.followMap = defaultdict(set)  # userId -> set of followeeId

#     def postTweet(self, userId: int, tweetId: int) -> None:
#         self.tweetMap[userId].append([self.count, tweetId])
#         self.count -= 1

#     def getNewsFeed(self, userId: int) -> List[int]:
#         res = []
#         minHeap = []

#         self.followMap[userId].add(userId)
#         for followeeId in self.followMap[userId]:
#             if followeeId in self.tweetMap:
#                 index = len(self.tweetMap[followeeId]) - 1
#                 count, tweetId = self.tweetMap[followeeId][index]
#                 heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

#         while minHeap and len(res) < 10:
#             count, tweetId, followeeId, index = heapq.heappop(minHeap)
#             res.append(tweetId)
#             if index >= 0:
#                 count, tweetId = self.tweetMap[followeeId][index]
#                 heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
#         return res

#     def follow(self, followerId: int, followeeId: int) -> None:
#         self.followMap[followerId].add(followeeId)

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         if followeeId in self.followMap[followerId]:
#             self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId = 1,tweetId = 0)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId = 2,followeeId = 3)
# print(obj.display())
# obj.unfollow(followerId = 5,followeeId = 3)