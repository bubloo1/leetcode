package arrays

import (
	"math"
)

func MaxSubArray(nums []int) int {
	maxSum := math.MinInt32
	currSum := 0

	for _, n := range nums {

		currSum += n
		if currSum > maxSum {
			maxSum = currSum
		}
		if currSum < 0 {
			currSum = 0
		}
	}
	return maxSum
}
