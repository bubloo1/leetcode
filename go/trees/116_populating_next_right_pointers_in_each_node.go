package trees

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

func connect(root *Node) *Node {

	queue := []*Node{root}

	for len(queue) > 0 {
		size := len(queue)

		for i := 0; i < len(queue); i++ {
			queue[i].Next = queue[i+1]
		}

		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]

			if node.Right != nil {
				queue = append(queue, node.Left)
			}

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
		}
	}
	return root
}
