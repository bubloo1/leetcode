from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedList = []

            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i + 1] if len(lists) > (i + 1) else None
                mergedList.append(self.mergeList(list1,list2))
            lists = mergedList
        return lists[0]
        
    def mergeList(self,l1,l2):
        dummy = temp = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummy.next

        



        # don't know if you can do like this in interview, but it works in leetcode
        # dummy = temp = ListNode(0)
        
        # newList = []

        # for ll in lists:
        #     while ll:
        #         newList.append(ll.val)
        #         ll = ll.next

        # newList.sort()
        
        # for i in range(len(newList)):
        #     temp.next = ListNode(newList[i])
        #     temp = temp.next

        # return dummy.next
newObject = Solution()
print(newObject.mergeKLists([[1,4,5],[1,3,4],[2,6]]))