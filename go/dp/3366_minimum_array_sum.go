package dp

func MinArraySum(nums []int, k int, op1 int, op2 int) int {
	n := len(nums)
	dp := make(map[[4]int]int)

	var dfs func(i, op1, op2 int) int
	dfs = func(i, op1, op2 int) int {
		if i >= n {
			return 0
		}

		key := [4]int{i, op1, op2}
		if val, exists := dp[key]; exists {
			return val
		}

		s := dfs(i+1, op1, op2) + nums[i]
		if op1 > 0 {
			s = min(s, dfs(i+1, op1-1, op2)+(nums[i]+1)/2)
		}
		if op2 > 0 && nums[i] >= k {
			s = min(s, dfs(i+1, op1, op2-1)+nums[i]-k)
		}
		if op1 > 0 && op2 > 0 && (nums[i]+1)/2 >= k {
			s = min(s, dfs(i+1, op1-1, op2-1)+(nums[i]+1)/2-k)
		}
		if op1 > 0 && op2 > 0 && nums[i] >= k {
			s = min(s, dfs(i+1, op1-1, op2-1)+(nums[i]-k+1)/2)
		}

		dp[key] = s
		return s
	}

	return dfs(0, op1, op2)
}

func sumOfArray(index int, nums []int) int {
	total := 0
	for i := index; i < len(nums); i++ {
		total += nums[i]
	}
	return total
}
