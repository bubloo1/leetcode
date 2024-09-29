package trees

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func diameterOfBinaryTree(root *TreeNode) int {

	maxLength := 0
	dfs(root, &maxLength)
	return maxLength
}

// func dfs(rootNode *TreeNode, maxLength *int) int {
// 	if rootNode == nil {
// 		return 0
// 	}

// 	left := dfs(rootNode.Left, maxLength)
// 	right := dfs(rootNode.Right, maxLength)
// 	*maxLength = max(left+right, *maxLength)
// 	return max(left, right) + 1
// }
