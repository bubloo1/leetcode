package main

func missingNumber(nums []int) int {
	var res int = len(nums)
	for i := 0; i < len(nums); i++ {
		res = res + (i - nums[i])
	}

	return res
}
