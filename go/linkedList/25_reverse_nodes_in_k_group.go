package linkeList

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	var dummy *ListNode = &ListNode{0, head}
	var groupPrev *ListNode = dummy

	for true {
		var kth *ListNode = getKth(groupPrev, k)

		if kth == nil {
			break
		}
		var groupNext *ListNode = kth.Next

		prev, curr := kth.Next, groupPrev.Next

		for curr != groupNext {
			temp := curr.Next
			curr.Next = prev
			prev = curr
			curr = temp
		}

		temp := groupPrev.Next
		// After reversing the current group of nodes,
		// kth is now the new head of the reversed group.
		// last node of first group as head
		groupPrev.Next = kth
		//Once the current group is reversed, the groupPrev pointer needs to be
		//moved to the end of the newly reversed group for the next iteration.
		// first node of first group as first node of second group
		//1 -> 2
		//2 -> 1 second group will start after 1
		groupPrev = temp
	}
	return dummy.Next
}

func getKth(curr *ListNode, k int) *ListNode {
	for curr != nil && k > 0 {
		curr = curr.Next
		k -= 1
	}
	return curr
}
