package main

func rob(nums []int) int {

	rob1, rob2, temp := 0, 0, 0

	for _, n := range nums {
		temp = max(n+rob1, rob2)
		rob1 = rob2
		rob2 = temp
	}
	return temp
	// time complexity Olog(n), space complexity Olog(n)
	// if len(nums) == 1 {
	// 	return nums[0]
	// }

	// var dp = make([]int, len(nums))
	// dp[0] = nums[0]
	// dp[1] = max(nums[0], nums[1])

	// for i := 2; i < len(nums); i++ {
	// 	dp[i] = max(nums[i]+dp[i-2], dp[i-1])
	// }
	// return dp[len(nums)-1]
}
