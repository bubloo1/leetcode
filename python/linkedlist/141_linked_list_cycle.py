# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # nodes_set = set()
        # temp = head
        # while temp:
        #     if temp in nodes_set:
        #         return True
        #     nodes_set.add(temp)
        #     temp = temp.next
        # return False

        if head is None:
            return False
        
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False