package arrays

import "fmt"

func IsZeroArray(nums []int, queries [][]int) bool {
	length := len(nums)
	pos := make([]int, length+1)
	prefix := 0
	for _, q := range queries {
		pos[q[0]]++
		pos[q[1]+1]--
	}
	fmt.Println(pos)
	for i, num := range nums {
		prefix += pos[i]
		if prefix < num {
			return false
		}
	}
	return true
}
