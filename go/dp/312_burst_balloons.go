package dp

func maxCoins(nums []int) int {
	var dfs func(left, right int) int
	dp := make(map[[2]int]int)
	nums = append([]int{1}, nums...)
	nums = append(nums, 1)

	dfs = func(left, right int) int {

		if left > right {
			return 0
		}

		if val, exits := dp[[2]int{left, right}]; exits {
			return val
		}
		dp[[2]int{left, right}] = 0

		for i := left; i < right+1; i++ {
			// logic here is we will pop this eleemnt last
			coins := nums[left-1] * nums[i] * nums[right+1]

			coins += dfs(left, i-1) + dfs(i+1, right)
			dp[[2]int{left, right}] = max(dp[[2]int{left, right}], coins)
		}

		return dp[[2]int{left, right}]
	}

	return dfs(1, len(nums)-2)
}
