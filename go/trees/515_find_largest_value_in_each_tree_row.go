package trees

import (
	"math"
)

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

func FindLargestValue(root *TreeNode) []int {
	if root == nil {
		return nil
	}

	var queue []*TreeNode
	var res []int

	queue = append(queue, root)
	for len(queue) > 0 {
		currMax := math.MinInt32
		levelSize := len(queue)

		for i := 0; i < levelSize; i++ {

			currNode := queue[0]
			queue = queue[1:]
			currMax = max(currMax, currNode.Val)

			if currNode.Left != nil {
				queue = append(queue, currNode.Left)
			}
			if currNode.Right != nil {
				queue = append(queue, currNode.Right)
			}
		}
		res = append(res, currMax)
	}

	return res
}
