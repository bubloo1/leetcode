# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse(Node):
            prev = None
            curr = Node

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        if head is None or head.next is None:
            return True
        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = reverse(slow.next)
        slow = slow.next
        dummy = head

        while slow != None:
            if dummy.val != slow.val:
                return False
            
            dummy = dummy.next
            slow = slow.next
        return True


  