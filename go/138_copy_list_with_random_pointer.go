package main

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {
	var oldToClone = make(map[*Node]*Node)
	currNode := head

	for currNode != nil {
		clone := &Node{Val: currNode.Val}
		oldToClone[currNode] = clone
		currNode = currNode.Next
	}

	currNode = head
	for currNode != nil {
		clone := oldToClone[currNode]
		clone.Next = oldToClone[currNode.Next]
		clone.Random = oldToClone[currNode.Random]
		currNode = currNode.Next
	}
	return oldToClone[head]

}
