package dp

func FindMaxForm(strs []string, m int, n int) int {
	var dfs func(i, m, n int) int
	var findNoOfOnesAndZeros func(currString string) (int, int)

	dp := make(map[[3]int]int)

	findNoOfOnesAndZeros = func(currString string) (int, int) {
		zeroes, ones := 0, 0
		for _, char := range currString {
			if char == '0' {
				zeroes++
			} else if char == '1' {
				ones++
			}
		}
		return zeroes, ones
	}

	dfs = func(i, m, n int) int {

		if i >= len(strs) {
			return 0
		}

		if val, exits := dp[[3]int{i, m, n}]; exits {
			return val
		}

		zereos, ones := findNoOfOnesAndZeros(strs[i])

		dp[[3]int{i, m, n}] = dfs(i+1, m, n)

		if zereos <= m && ones <= n {
			dp[[3]int{i, m, n}] = max(dp[[3]int{i, m, n}],
				1+dfs(i+1, m-zereos, n-ones))
		}
		return dp[[3]int{i, m, n}]

	}
	return dfs(0, m, n)
}
