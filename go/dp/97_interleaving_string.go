package dp

func IsInterleave(s1 string, s2 string, s3 string) bool {
	if len(s1)+len(s2) != len(s3) {
		return false
	}
	var dfs func(i int, j int, k int) bool
	dp := make(map[[3]int]bool)

	dfs = func(i, j, k int) bool {
		if k == len(s3) {
			return true
		}
		if val, exists := dp[[3]int{i, j, k}]; exists {
			return val
		}
		if i < len(s1) && s1[i] == s3[k] && dfs(i+1, j, k+1) {
			dp[[3]int{i, j, k}] = true
			return true
		}
		if j < len(s2) && s2[j] == s3[k] && dfs(i, j+1, k+1) {
			dp[[3]int{i, j, k}] = true
			return true
		}
		dp[[3]int{i, j, k}] = false
		return false
	}
	return dfs(0, 0, 0)

	// var dfs func(i int, j int, k int) bool

	// if len(s1)+len(s2) != len(s3) {
	// 		return false
	// }

	// dfs = func(i, j, k int) bool {
	// 	if k == len(s3) {
	// 		return true
	// 	}

	// 	if i < len(s1) && s1[i] == s3[k] && dfs(i+1, j, k+1) {
	// 		return true
	// 	}
	// 	if j < len(s2) && s2[j] == s3[k] && dfs(i, j+1, k+1) {
	// 		return true
	// 	}
	// 	return false
	// }
	// return dfs(0, 0, 0)
}
