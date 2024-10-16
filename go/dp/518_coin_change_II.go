package dp

func Change(amount int, coins []int) int {
	var dfs func(index, currSum int) int

	dp := make([][]int, len(coins))
	for i := range dp {
		dp[i] = make([]int, amount+1)

		for j := range dp[i] {
			dp[i][j] = -1
		}
	}

	dfs = func(index, currSum int) int {

		if amount == currSum {
			return 1
		}

		if index >= len(coins) || currSum > amount {
			return 0
		}

		if dp[index][currSum] != -1 {
			return dp[index][currSum]
		}

		combinations := 0

		combinations += dfs(index, currSum+coins[index]) + dfs(index+1, currSum)
		dp[index][currSum] = combinations

		return combinations
	}
	return dfs(0, 0)
}
