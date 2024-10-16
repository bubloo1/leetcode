package dp

import (
	"math"
)

func MinCut(s string) int {
	var dfs func(index int) int
	var isPlaindrome func(left, right int) bool

	dp := make([]int, len(s)+1)
	for i := range dp {
		dp[i] = math.MaxInt32
	}

	isPlaindrome = func(left, right int) bool {
		for left <= right {
			if s[left] != s[right] {
				return false
			}
			left++
			right--
		}
		return true
	}

	dfs = func(index int) int {
		if index >= len(s) {
			return 0
		}

		if dp[index] != math.MaxInt32 {
			return dp[index]
		}

		for j := index; j < len(s); j++ {
			if isPlaindrome(index, j) {
				dp[index] = min(dp[index], 1+dfs(j+1))
			}
		}
		return dp[index]
	}
	dfs(0)

	return dp[0] - 1
}
