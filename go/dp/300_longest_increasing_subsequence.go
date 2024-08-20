package dp

func LengthOfLIS(nums []int) int {

	dp := make([]int, len(nums))

	for i := range dp {
		dp[i] = 1
	}

	longestSequence := 0
	for i := len(nums) - 1; i >= 0; i-- {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] < nums[j] {
				dp[i] = max(dp[i], 1+dp[j])
				longestSequence = max(longestSequence, dp[i])
			}
		}
	}

	return longestSequence

	// using just recursion Olog(2^n)
	// var dfs func(i int, currSubset []int)
	// var ans = make([]int, 0)
	// dfs = func(i int, currSubset []int) {

	// 	if i >= len(nums) {
	// 		if len(currSubset) > len(ans) {
	// 			ans = make([]int, len(currSubset))
	// 			copy(ans, currSubset)
	// 		}
	// 		return
	// 	}

	// 	if len(currSubset) == 0 || nums[i] > currSubset[len(currSubset)-1] {
	// 		dfs(i+1, append(currSubset, nums[i]))
	// 	}

	// 	dfs(i+1, currSubset)
	// }
	// dfs(0, []int{})
	// return ans
}
