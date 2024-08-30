package arrays

func PlusOne(digits []int) []int {
	n := len(digits)

	for i := n - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}

	// If all digits are 9, we need to add a 1 at the beginning
	return append([]int{1}, digits...)
}
