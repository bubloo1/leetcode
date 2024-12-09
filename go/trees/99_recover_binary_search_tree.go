package trees

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// for this question only inorder works because inorder produces sorted sequence

func RecoverTree(root *TreeNode) {

	var inOrder func(node *TreeNode)
	var first, middle, last, prev *TreeNode

	// Helper function to perform in-order traversal
	inOrder = func(node *TreeNode) {
		if node == nil {
			return
		}

		// Traverse the left subtree
		inOrder(node.Left)

		// Detect swapped nodes
		if prev != nil && node.Val < prev.Val {
			// If this is the first occurrence of a disorder
			if first == nil {
				first = prev
				middle = node
			} else {
				last = node
			}

		}
		// Update the previous node
		prev = node

		// Traverse the right subtree
		inOrder(node.Right)
	}

	// Perform in-order traversal to find the two swapped nodes
	inOrder(root)

	// Swap the values of the two nodes to fix the BST
	if first != nil && last != nil {
		first.Val, last.Val = last.Val, first.Val
	} else {
		first.Val, middle.Val = middle.Val, first.Val
	}

	// var inOrder func(node *TreeNode)
	// var generateTree func(node *TreeNode)
	// var output []int
	// index := 0

	// inOrder = func(node *TreeNode) {
	// 	if node != nil {
	// 		inOrder(node.Left)
	// 		output = append(output, node.Val)
	// 		inOrder(node.Right)
	// 	}
	// }

	// generateTree = func(node *TreeNode) {

	// 	if node != nil {
	// 		generateTree(node.Left)
	// 		// if output[index] != node.Val {
	// 		node.Val = output[index]
	// 		index++
	// 		// }
	// 		output = append(output, node.Val)
	// 		generateTree(node.Right)
	// 	}
	// }

	// inOrder(root)
	// sort.Ints(output)
	// generateTree(root)
}
