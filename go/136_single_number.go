package main

func singleNumber(nums []int) int {
	var res int = 0
	for _, val := range nums {
		res = res ^ val
	}
	return res
}

// 0 -> 0000
// 4 -> 0100 -> 0100
// 1 -> 0001 -> 0101
// 2 -> 0010 -> 0111
// 1 -> 0001 -> 0110
// 2 -> 0010 -> 0100
