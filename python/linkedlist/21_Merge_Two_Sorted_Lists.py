from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # if not list2:
        #     return list1
        # if not list1:
        #     return list2

        # temp = dummy = ListNode(0)

        # while list1 and list2:

        #     if list1.val < list2.val:
        #         dummy.next = list1
        #         list1 = list1.next
        #     else:
        #         dummy.next = list2
        #         list2 = list2.next
        #     dummy = dummy.next
        
        # if list1:
        #     dummy.next = list1

        # if list2:
        #     dummy.next = list2
        
        # return temp.next

        if list1 == None:
            return list2
        
        if list2 == None:
            return list1
        
        if list1.val > list2.val:
            list1,list2 = list2, list1
        res = list1
        while list1 != None and list2 != None:
            temp = None
            while list1 != None and list1.val <= list2.val:
                temp = list1
                list1 = list1.next
            temp.next = list2
            list1,list2 = list2,list1
        return res

