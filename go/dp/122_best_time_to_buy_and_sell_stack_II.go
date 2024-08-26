package dp

func maxProfit(prices []int) int {
	curr := []int{0, 0}
	ahead := []int{0, 0}

	for index := len(prices) - 1; index >= 0; index-- {
		for buy := 0; buy <= 1; buy++ {
			profit := 0
			if buy == 1 {
				profit = max(prices[index]+ahead[0], ahead[1])
			} else {
				profit = max(-prices[index]+ahead[1], ahead[0])
			}
			curr[buy] = profit
		}
		ahead = curr
	}
	return curr[0]

	//  top down using tabulation
	// dp := make([][]int, len(prices)+1)

	// for i := range dp {
	// 	dp[i] = []int{0, 0}
	// }
	// fmt.Println("sfgfdgfg")
	// for index := len(prices) - 1; index >= 0; index-- {
	// 	for buy := 0; buy <= 1; buy++ {
	// 		profit := 0
	// 		if buy == 1 {
	// 			profit = max(prices[index]+dp[index+1][0], dp[index+1][1])
	// 		} else {
	// 			profit = max(-prices[index]+dp[index+1][1], dp[index+1][0])
	// 		}
	// 		dp[index][buy] = profit
	// 	}
	// }
	// return dp[0][0]

	// using memo dp array
	// var dfs func(index int, buy int) int
	// dp := make([][]int, len(prices))

	// for i := range dp {
	// 	dp[i] = []int{-1, -1}
	// }

	// dfs = func(index int, buy int) int {
	// 	if index >= len(prices) {
	// 		return 0
	// 	}
	// 	if dp[index][buy] != -1 {
	// 		return dp[index][buy]
	// 	}
	// 	profit := 0
	// 	if buy == 1 {
	// 		profit = max(prices[index]+dfs(index+1, 0), dfs(index+1, 1))
	// 	} else {
	// 		profit = max(-prices[index]+dfs(index+1, 1), dfs(index+1, 0))
	// 	}
	// 	dp[index][buy] = profit
	// 	return profit
	// }
	// return dfs(0, 0)

	// brute force recursion try every possible way
	// var dfs func(index int, buy bool) int
	// dfs = func(index int, buy bool) int {
	// 	if index >= len(prices) {
	// 		return 0
	// 	}

	// 	if buy {
	// 		return max(prices[index]+dfs(index+1, false), dfs(index+1, true))
	// 	} else {
	// 		return max(-prices[index]+dfs(index+1, true), dfs(index+1, false))
	// 	}

	// }
	// return dfs(0, false)
}
