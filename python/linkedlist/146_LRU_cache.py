class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    #first node between hwead and tail | 0 | 0 |  ->  | 1 | 1 |  ->  | 0 | 0
    #second node between first node and tail | 0 | 0 |  ->  | 1 | 1 |  ->  | 2 | 2 |  ->  | 0 | 0 |
    def insert(self,node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def remove(self,node):
        prev,nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.cache[key].val
        return - 1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
    
        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

lruCache = LRUCache(2)
print(lruCache.put(1,1))
print(lruCache.put(2,2))
print(lruCache.get(1))
print(lruCache.put(3,3))
print(lruCache.get(2))
print(lruCache.put(4,4))
print(lruCache.get(1))
print(lruCache.get(3))
print(lruCache.get(4))


    
# put
# 1 -> 2 -> 3 -> 4 -> 5 
# get(1)
# 2 -> 3 -> 4 -> 5 -> 1
# get(4)
# 2 -> 3 -> 5 -> 1 -> 4