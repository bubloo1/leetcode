package bitmap

func missingNumber(nums []int) int {
	// range is 0 .. n
	// we are adding  num[i] and subtracting i, the i which is not including
	// in array will remain
	var res int = len(nums)
	for i := 0; i < len(nums); i++ {
		res = res + (i - nums[i])
	}

	return res
}
