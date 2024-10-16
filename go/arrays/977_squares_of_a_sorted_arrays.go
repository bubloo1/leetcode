package arrays

import (
	"math"
)

func SortedSquares(nums []int) []int {
	lenOfNums := len(nums)
	left, right := 0, lenOfNums-1
	res := make([]int, lenOfNums)

	for left <= right {
		if math.Abs(float64(nums[left])) > math.Abs(float64(nums[right])) {
			res[right-left] = nums[left] * nums[left]
			left++
		} else {
			res[right-left] = nums[right] * nums[right]
			right--
		}
	}
	return res
}
