package dp

import "fmt"

func LongestCommonSubsequence(text1 string, text2 string) int {

	dp := make([][]int, len(text1)+1)

	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, len(text2)+1)
	}

	for i := len(text1) - 1; i >= 0; i-- {
		for j := len(text2) - 1; j >= 0; j-- {
			if text1[i] == text2[j] {
				dp[i][j] = 1 + dp[i+1][j+1]
			} else {
				dp[i][j] = max(dp[i][j+1], dp[i+1][j])
			}
		}
	}
	fmt.Println(dp, "dpd")
	return dp[0][0]

	// var findLongestCommmonSubSeq func(i int, j int) int
	// lenOfText1 := len(text1)
	// lenOfText2 := len(text2)
	// dp := make([][]int, lenOfText1)

	// for i := range dp {
	// 	dp[i] = make([]int, lenOfText2)
	// }

	// findLongestCommmonSubSeq = func(i, j int) int {
	// 	if i >= lenOfText1 || j >= lenOfText2 {
	// 		return 0
	// 	} else if dp[i][j] != 0 {
	// 		return dp[i][j]
	// 	} else if text1[i] == text2[j] {
	// 		dp[i][j] = 1 + findLongestCommmonSubSeq(i+1, j+1)
	// 	} else {
	// 		dp[i][j] = max(findLongestCommmonSubSeq(i+1, j), findLongestCommmonSubSeq(i, j+1))
	// 	}
	// 	return dp[i][j]
	// }

	// return findLongestCommmonSubSeq(0, 0)
}
