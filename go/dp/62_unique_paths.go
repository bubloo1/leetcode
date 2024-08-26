package dp

func UniquePaths(m int, n int) int {
	var findPath func(r int, l int, path int) int
	dp := make([][]int, m)

	for i := range dp {
		dp[i] = make([]int, n)
	}

	findPath = func(r int, l int, path int) int {

		if r < 0 || l < 0 {
			return 0
		}

		if r == 0 && l == 0 {
			return 1
		}

		if dp[r][l] != 0 {
			return dp[r][l]
		}

		dp[r][l] = findPath(r-1, l, path) + findPath(r, l-1, path)
		return dp[r][l]
	}
	return findPath(m-1, n-1, 0)
}
