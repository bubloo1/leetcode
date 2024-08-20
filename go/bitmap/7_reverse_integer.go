package bitmap

import "math"

func reverse(x int) int {
	var res int = 0
	var negative bool = x < 0

	if negative {
		x = -x
	}
	for x > 0 {
		if math.MaxInt32/10 < res {
			return 0
		}
		res = res*10 + x%10
		x = x / 10
	}

	if negative {
		return -res
	}
	return res
}
