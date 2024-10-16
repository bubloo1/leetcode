package dp

func MaxSumAfterPartitioning(arr []int, k int) int {
	dp := make([]int, len(arr)+1)
	var dfs func(index int) int

	for i := range dp {
		dp[i] = -1
	}

	dfs = func(index int) int {
		if dp[index] != -1 {
			return dp[index]
		}

		currMax := 0
		res := 0

		for j := index; j < min(len(arr), index+k); j++ {
			currMax = max(currMax, arr[j])
			windowSize := j - index + 1
			res = max(res, dfs(j+1)+currMax*windowSize)
		}
		dp[index] = res
		return res
	}

	return dfs(0)
}
