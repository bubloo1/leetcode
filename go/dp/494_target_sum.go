package dp

func FindTargetSumWays(nums []int, target int) int {
	var dfs func(index int, currSum int) int
	dp := make(map[int]map[int]int, len(nums)+1)

	dfs = func(index int, currSum int) int {
		if index >= len(nums) {
			if currSum == target {
				return 1
			}
			return 0
		}

		if _, exists := dp[index]; !exists {
			dp[index] = make(map[int]int)
		}

		if val, exists := dp[index][currSum]; exists {
			return val
		}

		dp[index][currSum] = dfs(index+1, currSum+nums[index]) + dfs(index+1, currSum-nums[index])
		return dp[index][currSum]
	}

	return dfs(0, 0)
}
