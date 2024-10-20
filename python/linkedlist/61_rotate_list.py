from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
        
        temp = head
        length = 0    
        while temp.next:
            temp = temp.next
            length += 1
        
        temp.next = head
        k = k % length
        end = length - k

        while end:
            temp = temp.next
            end -= 1
        
        head = temp.next
        temp.next = None
    
        return head