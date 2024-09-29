package recursion

func LastRemaining(n int) int {
	var helper func(n int, left bool) int
	helper = func(n int, left bool) int {
		if n == 1 {
			return 1
		}

		if left || n%2 == 1 {
			return 2 * helper(n/2, !left)
		} else {
			return 2*helper(n/2, !left) - 1
		}
	}
	return helper(n, true)
}
