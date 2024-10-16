package dp

func NumDistinct(s string, t string) int {

	var dfs func(i, j int) int
	dp := make(map[[2]int]int)

	dfs = func(i, j int) int {

		if j == len(t) {
			return 1
		}
		if i == len(s) {
			return 0
		}

		if val, exists := dp[[2]int{i, j}]; exists {
			return val
		}

		if s[i] == t[j] {
			dp[[2]int{i, j}] = dfs(i+1, j+1) + dfs(i+1, j)
		} else {
			dp[[2]int{i, j}] = dfs(i+1, j)
		}

		return dp[[2]int{i, j}]
	}

	return dfs(0, 0)
}
