package main

import (
	"math"
)

func maxSubArray(nums []int) int {
	var currMax int = math.MinInt32
	var currSum int = 0
	for i := range nums {
		currSum += nums[i]
		if currSum > currMax {
			currMax = currSum
		}
		if currSum < 0 {
			currSum = 0
		}
	}
	return currMax
}
