package dp

func MinDistance(word1 string, word2 string) int {
	// Create a DP table to store results of subproblems
	dp := make([][]int, len(word1)+1)
	for i := range dp {
		dp[i] = make([]int, len(word2)+1)
		for j := 0; j < len(word2)+1; j++ {
			dp[i][j] = -1 // Initialize with -1 to indicate uncomputed states
		}
	}

	var dfs func(i, j int) int
	dfs = func(i, j int) int {
		if dp[i][j] != -1 {
			return dp[i][j]
		}

		// Base cases
		if i == len(word1) {
			return len(word2) - j
		}
		if j == len(word2) {
			return len(word1) - i
		}

		if word1[i] == word2[j] {
			dp[i][j] = dfs(i+1, j+1)
		} else {
			insert := 1 + dfs(i, j+1)
			delete := 1 + dfs(i+1, j)
			replace := 1 + dfs(i+1, j+1)
			dp[i][j] = min(insert, delete, replace)
		}

		return dp[i][j]
	}

	return dfs(0, 0)
}
