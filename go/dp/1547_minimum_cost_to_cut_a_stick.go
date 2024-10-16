package dp

import "math"

func MinCost(n int, cuts []int) int {
	dp := make(map[[2]int]int)
	var dfs func(left, right int) int

	dfs = func(left, right int) int {
		if right-left == 1 {
			return 0
		}

		if val, exists := dp[[2]int{left, right}]; exists {
			return val
		}

		res := math.MaxInt32

		for _, c := range cuts {
			if left < c && c < right {
				res = min(res, (right-left)+dfs(left, c)+dfs(c, right))
			}
		}

		if res == math.MaxInt32 {
			res = 0
		}

		dp[[2]int{left, right}] = res
		return res
	}
	return dfs(0, n)
}
