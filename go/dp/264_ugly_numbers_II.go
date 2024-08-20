package dp

func nthUglyNumber(n int) int {
	dp := make([]int, n+1)
	dp[1] = 1
	i2, i3, i5 := 1, 1, 1

	for i := 2; i <= n; i++ {
		dp[i] = min(dp[i2]*2, dp[i3]*3, dp[i5]*5)

		if dp[i] == dp[i2]*2 {
			i2++
		}
		if dp[i] == dp[i3]*3 {
			i3++
		}
		if dp[i] == dp[i5]*5 {
			i5++
		}
	}

	return dp[n]
}
