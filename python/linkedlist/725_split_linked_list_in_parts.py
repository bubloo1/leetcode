from typing import Optional,List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
      
        temp = head
        length = 0

        while temp:
            length += 1
            temp = temp.next
        
        PartLen = length//k
        rem = length%k

        temp = head
        res = []
        for i in range(k):
            partHead = temp
            partSize = PartLen + (1 if rem > 0 else 0)
            rem -= 1

            for j in range(partSize - 1):
                if temp:
                    temp = temp.next

            if temp:
                nextPart = temp.next
                temp.next = None
                temp = nextPart
            
            res.append(partHead)

        return res


ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)
ll.next.next.next.next.next = ListNode(6)
ll.next.next.next.next.next.next = ListNode(7)
ll.next.next.next.next.next.next.next = ListNode(8)
ll.next.next.next.next.next.next.next.next = ListNode(9)
ll.next.next.next.next.next.next.next.next.next = ListNode(10)
newObject = Solution()
print(newObject.splitListToParts(ll,3))

