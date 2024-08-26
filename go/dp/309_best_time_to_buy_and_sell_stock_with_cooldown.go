package dp

func MaxProfit(prices []int) int {
	var dfs func(index int, buy int) int
	dp := make([][]int, len(prices)+1)

	for i := range dp {
		dp[i] = []int{-1, -1}
	}
	dfs = func(index int, buy int) int {
		if index >= len(prices) {
			return 0
		}

		if dp[index][buy] != -1 {
			return dp[index][buy]
		}

		cooldown := dfs(index+1, buy)

		if buy == 0 {
			dp[index][buy] = max(-prices[index]+dfs(index+1, 1), cooldown)
		} else {
			dp[index][buy] = max(prices[index]+dfs(index+2, 0), cooldown)
		}
		return dp[index][buy]
	}
	return dfs(0, 0)

	// var dfs func(day int) int

	// dfs = func(day int) int {

	// 	if day >= len(prices) {
	// 		return 0
	// 	}

	// 	skip := dfs(day + 1)

	// 	maxProfit := 0

	// 	if day < len(prices)-1 {
	// 		profit := prices[day+1] - prices[day] + dfs(day+2)
	// 		if profit > maxProfit {
	// 			maxProfit = profit
	// 		}
	// 	}

	// 	return max(skip, maxProfit)
	// }
	// return dfs(0)
}
