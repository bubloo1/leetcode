package dp

func numDecodings(s string) int {

	dp := make([]int, len(s)+1)

	dp[0] = 1
	if s[0] == '0' {
		dp[1] = 0
	} else {
		dp[1] = 1
	}

	for i := 2; i < len(s)+1; i++ {
		firstDigit := s[i-1 : i]
		secondDigit := s[i-2 : i]

		if firstDigit >= "1" {
			dp[i] += dp[i-1]
		}
		if secondDigit >= "10" && secondDigit <= "26" {
			dp[i] += dp[i-2]
		}
	}

	return dp[len(s)]

	// recursive approch getting memory limit exceed error
	// var dfs func(int) int
	// dfs = func(index int) int {
	// 	if index == len(s) {
	// 		return 1
	// 	}

	// 	if s[index] == '0' {
	// 		return 0
	// 	}

	// 	ways := dfs(index + 1)

	// 	if index < len(s)-1 && (s[index] == '1' || (s[index] == '2' && s[index+1] <= '6')) {
	// 		ways += dfs(index + 2)
	// 	}
	// 	return ways
	// }

	// if len(s) == 0 {
	// 	return 0
	// }
	// return dfs(0)
}
