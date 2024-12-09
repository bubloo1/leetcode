package arrays

func checkSubarraySum(nums []int, k int) bool {
	remainder := make(map[int]int)
	total := 0
	remainder[0] = -1
	for i, n := range nums {
		total += n
		r := total % k
		if _, exists := remainder[r]; !exists {
			remainder[r] = i
		} else if i-remainder[r] > 1 {
			return true
		}
	}
	return false
}
