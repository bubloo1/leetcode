package main

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
		groupPrev.Next = kth
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
