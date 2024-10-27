# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # while headA:
        #     temp = headB
        #     while temp is not None:
        #         if temp == headA:
        #             return temp
        #         temp = temp.next
        #     headA = headA.next
        # return None
    	
        # nodes_set = set()

        # while headA:
        #     nodes_set.add(headA)
        #     headA = headA.next
        
        # while headB:
        #     if headB in nodes_set:
        #         return headB
        #     headB = headB.next
        # return None
        
        d1 = headA
        d2 = headB
        while d1 != d2:
            d1 = headB if d1 == None else d1.next
            d2 = headA if d2 == None else d2.next
        return d1