package dp

func MinInsertions(s string) int {

	var dfs func(start, end int) int
	dp := make(map[[2]int]int)
	dfs = func(start, end int) int {

		if start >= end {
			return 0
		}

		if val, exists := dp[[2]int{start, end}]; exists {
			return val
		}

		if s[start] == s[end] {
			dp[[2]int{start, end}] = dfs(start+1, end-1)
		} else {
			dp[[2]int{start, end}] = 1 + min(dfs(start+1, end), dfs(start, end-1))
		}
		return dp[[2]int{start, end}]
	}
	return dfs(0, len(s)-1)

	// var dfs func(start, end int) int

	// dfs = func(start, end int) int {

	// 	if start >= end {
	// 		return 0
	// 	}

	// 	res := 1
	// 	if s[start] == s[end] {
	// 		res = dfs(start+1, end-1)
	// 	} else {
	// 		res = 1 + min(dfs(start+1, end), dfs(start, end-1))
	// 	}
	// 	return res
	// }
	// return dfs(0, len(s)-1)
}
