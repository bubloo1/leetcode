from typing import List,Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        evenHead = even
        
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        odd.next = evenHead
        return head

newObject = Solution()
root = ListNode(1)
root.next =ListNode(2)
root.next.next =ListNode(3)
root.next.next.next =ListNode(4)
root.next.next.next.next =ListNode(5)

newObject.oddEvenList(root)
# newObject.display()