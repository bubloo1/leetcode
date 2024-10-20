package bitmap

func CountMaxOrSubsets(nums []int) int {
	var dfs func(index, currOr int) int
	maxOr := 0
	dp := make([][]int, len(nums))

	for _, n := range nums {
		maxOr |= n
	}

	for i := range dp {
		dp[i] = make([]int, maxOr+1)
		for j := range dp[i] {
			dp[i][j] = -1
		}
	}
	dfs = func(index, currOr int) int {
		if index >= len(nums) {
			if currOr == maxOr {
				return 1
			} else {
				return 0
			}
		}

		if dp[index][currOr] != -1 {
			return dp[index][currOr]
		}

		dp[index][currOr] = dfs(index+1, currOr) + dfs(index+1, currOr|nums[index])
		return dp[index][currOr]
	}
	return dfs(0, 0)
}
