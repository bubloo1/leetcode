package trees

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	var dfs func(*TreeNode) int
	// var res int = 0

	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		// left := 1 + dfs(node.Left)
		// right := 1 + dfs(node.Right)
		// res := max(res, left, right)
		return 1 + max(dfs(node.Left), dfs(node.Right))
	}
	return dfs(root)
}
