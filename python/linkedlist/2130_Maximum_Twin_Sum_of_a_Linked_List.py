# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        def reverse(Node):
            prev = None
            curr = Node

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = reverse(slow.next)
            
        res = 0
        while prev:
            res = max(res, prev.val + head.val)
            prev = prev.next
            head = head.next
        
        return res


        