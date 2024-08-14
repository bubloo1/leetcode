package main

func countBits(n int) []int {

	// dp soln
	var dp = make([]int, n+1)
	var offset int = 1

	for i := 1; i <= n; i++ {
		if offset*2 == i {
			offset = i
		}
		dp[i] = 1 + dp[i-offset]
	}

	return dp

	// brute force
	// var num int = 0
	// var res = make([]int, n+1)

	// for j := 0; j < len(res); j++ {
	// 	res[j] = 0
	// }

	// for i := 0; i <= n; i++ {
	// 	num = i
	// 	for num > 0 {
	// 		res[i] = res[i] + num%2
	// 		num = num >> 1
	// 	}
	// }
	// return res
}
