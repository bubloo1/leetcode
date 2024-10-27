package arrays

import "math"

func MinSubArrayLen(target int, nums []int) int {

	currTotal, res, l := 0, math.MaxInt32, 0
	for r := range nums {
		currTotal += nums[r]
		for currTotal >= target {
			res = min(res, r-l+1)
			currTotal -= nums[l]
			l += 1
		}
	}
	if res == math.MaxInt32 {
		return 0
	}
	return res
}
