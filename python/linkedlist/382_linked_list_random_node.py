# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.List = []

        while head:
            self.List.append(head.val)
            head = head.next
        

    def getRandom(self) -> int:
        return self.List[random.randrange(len(self.List))]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()