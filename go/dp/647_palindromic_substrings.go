package dp

import "fmt"

func countSubstrings(s string) int {

	n := len(s)
	dp := make([][]int, n)
	count := 0
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		dp[i][i] = 1
		count += 1
	}

	for i := range n - 1 {
		if s[i] == s[i+1] {
			dp[i][i+1] = 1
			count += 1
		}
	}

	for length := 3; length <= n; length++ {
		for i := 0; i < n-length+1; i++ {
			j := i + length - 1
			if s[i] == s[j] && dp[i+1][j-1] == 1 {
				dp[i][j] = 1
				count += 1
			}
		}
	}
	fmt.Println(dp, "dp")
	return count
}
