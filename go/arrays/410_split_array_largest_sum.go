package arrays

import (
	"math"
)

func SplitArray(nums []int, k int) int {

	var canSplit func(largest int) bool
	canSplit = func(largest int) bool {
		subArray := 0
		currSum := 0

		for _, n := range nums {
			currSum += n
			if currSum > largest {
				subArray += 1
				currSum = n
			}
		}
		return subArray+1 <= k
	}
	l, r := findMax(nums), sum(nums)
	res := r
	for l <= r {
		mid := l + ((r - l) / 2)
		if canSplit(mid) {
			res = mid
			r = mid - 1
		} else {
			l = mid + 1
		}
	}

	return res
	// brute force solution n^2 * m
	// var dfs func(index, currSubArray int) int
	// dp := make(map[[2]int]int)

	// dfs = func(index, currSubArray int) int {
	// 	if val, exists := dp[[2]int{index, currSubArray}]; exists {
	// 		return val
	// 	}

	// 	if currSubArray == k-1 {
	// 		// fmt.Print(nums[index:])
	// 		return sum(nums[index:])
	// 	}

	// 	currMaxSum := 0
	// 	res := math.MaxInt32
	// 	for i := index; i < len(nums); i++ {
	// 		currMaxSum += nums[i]
	// 		maxSum := max(currMaxSum, dfs(i+1, currSubArray+1))
	// 		res = min(res, maxSum)
	// 	}
	// 	dp[[2]int{index, currSubArray}] = res
	// 	return res
	// }
	// return dfs(0, 0)
}

func sum(array []int) int {
	total := 0
	for i := range array {
		total += array[i]
	}
	return total
}

func findMax(array []int) int {
	maxVal := math.MinInt
	for _, num := range array {
		if num > maxVal {
			maxVal = num
		}
	}
	return maxVal
}
