package dp

func Jump(nums []int) int {

	l, r, res := 0, 0, 0

	for r < len(nums)-1 {
		maxJump := 0

		for i := l; i <= r; i++ {
			maxJump = max(i+nums[i], maxJump)
		}
		l = r + 1
		r = maxJump
		res++
	}
	return res

	// var findMiniJumpsReq func(position, count int) int
	// lenOfNums := len(nums) - 1

	// findMiniJumpsReq = func(position, count int) int {

	// 	if position > lenOfNums {
	// 		return math.MaxInt32
	// 	}

	// 	if position == lenOfNums {
	// 		return count
	// 	}

	// 	maxJump := min(position+nums[position], lenOfNums)
	// 	res := math.MaxUint32

	// 	for nextJump := position + 1; nextJump <= maxJump; nextJump++ {
	// 		res = min(findMiniJumpsReq(nextJump, count+1), res)
	// 	}
	// 	return res
	// }
	// return findMiniJumpsReq(0, 0)
}
