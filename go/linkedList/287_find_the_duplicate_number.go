package linkeList

func findDuplicate(nums []int) int {

	slow := nums[0]
	fast := nums[0]

	for true {
		slow = nums[slow]
		fast = nums[nums[fast]]
		if slow == fast {
			break
		}
	}

	fast = nums[0]
	for slow != fast {
		slow = nums[slow]
		fast = nums[fast]
	}
	return slow

	// var numsSet = make(map[int]struct{})

	// for _, n := range nums {
	// 	if _, exists := numsSet[n]; exists {
	// 		return n
	// 	} else {
	// 		numsSet[n] = struct{}{}
	// 	}
	// }
	// return -1

	// sort.Ints(nums)

	// for i := 0; i < len(nums)-2; i++ {
	// 	if nums[i] == nums[i+1] {
	// 		return nums[i]
	// 	}
	// }
	// return -1
}
