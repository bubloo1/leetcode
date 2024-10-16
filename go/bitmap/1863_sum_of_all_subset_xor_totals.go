package bitmap

func subsetXORSum(nums []int) int {
	var dfs func(i, total int) int
	dfs = func(i, total int) int {
		if i == len(nums) {
			return total
		}

		return dfs(i+1, total^nums[i]) + dfs(i+1, total)
	}

	return dfs(0, 0)
}
