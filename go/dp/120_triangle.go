package dp

func minimumTotal(triangle [][]int) int {
	var dfs func(i, j int) int
	dp := make(map[[2]int]int)

	dfs = func(i, j int) int {
		if i >= len(triangle) {
			return 0
		}

		if val, exists := dp[[2]int{i, j}]; exists {
			return val
		}

		left := dfs(i+1, j)
		right := dfs(i+1, j+1)

		dp[[2]int{i, j}] = triangle[i][j] + min(left, right)
		return dp[[2]int{i, j}]
	}

	return dfs(0, 0)
}
