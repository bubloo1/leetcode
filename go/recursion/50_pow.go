package recursion

import "math"

func MyPow(x float64, n int) float64 {
	var backtrack func(x float64, n int) float64

	backtrack = func(x float64, n int) float64 {
		if x == 0 {
			return 0
		}
		if n == 0 {
			return 1
		}

		res := backtrack(x*x, n/2)

		if n%2 != 0 {
			return x * res
		} else {
			return res
		}
	}
	ans := backtrack(x, int(math.Abs(float64(n))))
	if n < 0 {
		return 1 / ans
	}
	return ans
}
