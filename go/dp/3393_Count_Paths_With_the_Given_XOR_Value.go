package dp

func countPathsWithXorValue(grid [][]int, k int) int {
	MOD := 1e9 + 7
	m := len(grid)
	n := len(grid[0])
	var findPath func(r int, l int, path int) int
	dp := make(map[[3]int]int)

	findPath = func(r int, l int, pathSum int) int {

		if r < 0 || l < 0 {
			return 0
		}

		if r == 0 && l == 0 {
			if pathSum == k {
				return 1
			}
			return 0
		}

		if val, exits := dp[[3]int{r, l, pathSum}]; exits {
			return val
		}
		ans := 0
		if r-1 >= 0 {
			ans += findPath(r-1, l, pathSum^grid[r-1][l]) % int(MOD)
		}
		if l-1 >= 0 {
			ans += findPath(r, l-1, pathSum^grid[r][l-1]) % int(MOD)
		}
		dp[[3]int{r, l, pathSum}] = ans
		return ans
	}
	return findPath(m-1, n-1, grid[m-1][n-1]) % int(MOD)
}
