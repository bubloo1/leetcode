package arrays

import "fmt"

func SubarraysDivByK(nums []int, k int) int {

	prefix := map[int]int{0: 1}
	currSum, count := 0, 0
	for _, val := range nums {
		currSum += val
		rem := currSum % k
		if rem < 0 {
			rem += k
		}
		if val, exits := prefix[rem]; exits {
			fmt.Println(rem, "rem")
			count += val
		}
		prefix[rem]++
	}

	// count := 0
	// for i := 0; i < len(nums); i++ {
	// 	currSum := 0
	// 	for j := i; j < len(nums); j++ {
	// 		currSum += nums[j]
	// 		if currSum%k == 0 {
	// 			count += 1
	// 		}
	// 	}
	// }
	// return count
	return count
}
