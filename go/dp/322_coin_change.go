package dp

func CoinChange(coins []int, amount int) int {

	dp := make([]int, amount+1)

	for i, _ := range dp {
		dp[i] = amount + 1
	}

	dp[0] = 0

	for a := 1; a < amount+1; a++ {
		for _, c := range coins {
			if a-c >= 0 {
				dp[a] = min(dp[a], 1+dp[a-c])
			}
		}
	}

	if dp[amount] != amount+1 {
		return dp[amount]
	}
	return -1
	// brute force using recursion O(2 ^ n) tc
	// var backtrack func(index, currSum, CoinsCount int) int
	// ans := math.MaxInt32

	// backtrack = func(index, currSum, coinsCount int) int {

	// 	if currSum > amount || index >= len(coins) {
	// 		return 0
	// 	}

	// 	if amount == currSum {
	// 		return coinsCount
	// 	}

	// 	res := backtrack(index, coins[index]+currSum, coinsCount+1)

	// 	if res != 0 {
	// 		ans = min(res, ans)
	// 	}
	// 	res2 := backtrack(index+1, currSum, coinsCount)

	// 	if res2 != 0 {
	// 		ans = min(res2, ans)
	// 	}

	// 	return ans
	// }
	// result := backtrack(0, 0, 0)

	// if result == math.MaxInt32 {
	// 	return -1
	// }
	// return result
}
