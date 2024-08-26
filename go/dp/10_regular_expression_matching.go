package dp

// fmt.Sprintf("%v,%v", i, j) can use this to make a key in string format using i and j
func IsMatch(s string, p string) bool {

	var dfs func(i int, j int) bool
	dp := make(map[int]map[int]bool)

	for i := 0; i < len(s)+1; i++ {
		dp[i] = make(map[int]bool)

	}

	dfs = func(i, j int) bool {
		if i == len(s) && j == len(p) {
			return true
		}
		if j == len(p) {
			return false
		}
		if val, exits := dp[i][j]; exits {
			return val
		}

		match := (i < len(s) && (s[i] == p[j] || p[j] == '.'))
		var res bool
		if (j+1) < len(p) && p[j+1] == '*' {
			// don't use star or use "*"
			res = (dfs(i, j+2) || (match && dfs(i+1, j)))
		} else {
			res = (match && dfs(i+1, j+1))
		}
		dp[i][j] = res
		return res
	}

	return dfs(0, 0)

	// var dfs func(i int, j int) bool

	// dfs = func(i, j int) bool {

	// 	if i == len(s) && j == len(p) {
	// 		return true
	// 	}
	// 	if j == len(p) {
	// 		return false
	// 	}

	// 	match := (i < len(s) && (s[i] == p[j] || p[j] == '.'))

	// 	if (j+1) < len(p) && p[j+1] == '*' {
	// 		// don't use start or use "*"
	// 		return dfs(i, j+2) || (match && dfs(i+1, j))
	// 	} else {
	// 		return match && dfs(i+1, j+1)
	// 	}
	// }
	// return dfs(0, 0)
}
