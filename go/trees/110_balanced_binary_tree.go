package trees

import "math"

type BalancedTree struct {
	Balance bool
	Height  int
}

func isBalanced(root *TreeNode) bool {
	return dfs(root).Balance
}

func dfs(root *TreeNode) BalancedTree {

	if root == nil {
		return BalancedTree{true, 0}
	}

	left := dfs(root.Left)
	right := dfs(root.Right)
	balanced := (left.Balance && right.Balance && int(math.Abs(float64(left.Height)-
		float64(right.Height))) <= 1)

	return BalancedTree{balanced, 1 + max(left.Height, right.Height)}
}
