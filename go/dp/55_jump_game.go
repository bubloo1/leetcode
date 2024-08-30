package dp

func CanJump(nums []int) bool {
	goal := len(nums) - 1

	for i := len(nums) - 1; i >= 0; i-- {
		if i+nums[i] >= goal {
			goal = i
		}
	}

	return goal == 0

	// var dfs func(position int) bool

	// dfs = func(position int) bool {
	// 	if position >= len(nums)-1 {
	// 		return true
	// 	}

	// 	currMaxJump := min(position+nums[position], len(nums)-1)

	// 	for nextPos := position + 1; nextPos <= currMaxJump; nextPos++ {
	// 		if dfs(nextPos) {
	// 			return true
	// 		}
	// 	}

	// 	return false
	// }

	// return dfs(0)
}
