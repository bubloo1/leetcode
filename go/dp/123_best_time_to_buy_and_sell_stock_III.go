package dp

func MaxProfit_3(prices []int) int {
	n := len(prices)
	// Memoization table
	memo := make([][][]int, n)
	for i := range memo {
		memo[i] = make([][]int, 2) // 2 states: canBuy = true/false
		for j := range memo[i] {
			memo[i][j] = make([]int, 3) // Up to 2 transactions
			for k := range memo[i][j] {
				memo[i][j][k] = -1
			}
		}
	}

	// Helper function for recursion with memoization
	var dfs func(i, canBuy, transactionsLeft int) int
	dfs = func(i, canBuy, transactionsLeft int) int {
		if i == n || transactionsLeft == 0 {
			return 0
		}

		if memo[i][canBuy][transactionsLeft] != -1 {
			return memo[i][canBuy][transactionsLeft]
		}

		// Don't take action today
		maxProfit := dfs(i+1, canBuy, transactionsLeft)

		if canBuy == 1 {
			// Option to buy
			maxProfit = max(maxProfit, -prices[i]+dfs(i+1, 0, transactionsLeft))
		} else {
			// Option to sell
			maxProfit = max(maxProfit, prices[i]+dfs(i+1, 1, transactionsLeft-1))
		}

		memo[i][canBuy][transactionsLeft] = maxProfit
		return maxProfit
	}

	return dfs(0, 1, 2)

	// if len(prices) == 0 {
	// 	return 0
	// }

	// firstBuy, firstSell := -1<<31, 0
	// secondBuy, secondSell := -1<<31, 0

	// for _, price := range prices {
	// 	// Max profit after first buy
	// 	firstBuy = max(firstBuy, -price)
	// 	// Max profit after first sell
	// 	firstSell = max(firstSell, firstBuy+price)
	// 	// Max profit after second buy
	// 	secondBuy = max(secondBuy, firstSell-price)
	// 	// Max profit after second sell
	// 	secondSell = max(secondSell, secondBuy+price)
	// }

	// return secondSell
}
