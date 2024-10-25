package dp

import (
	"math"
)

func MinPathSum(grid [][]int) int {
	m, n := len(grid), len(grid[0])

	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
		for j := range dp[i] {
			dp[i][j] = -1
		}
	}

	var dfs func(i, j int) int
	dfs = func(i, j int) int {

		if i >= m || j >= n {
			return math.MaxInt32
		}

		if i == m-1 && j == n-1 {
			return grid[i][j]
		}

		if dp[i][j] != -1 {
			return dp[i][j]
		}

		right := dfs(i, j+1)
		down := dfs(i+1, j)
		dp[i][j] = grid[i][j] + min(right, down)

		return dp[i][j]
	}

	return dfs(0, 0)
}
