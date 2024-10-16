package bitmap

func SingleNumber(nums []int) []int {
	xor := 0
	for _, n := range nums {
		xor ^= n
	}

	diffBit := 1

	for xor&diffBit == 0 {
		diffBit = diffBit << 1
	}

	a, b := 0, 0

	for _, n := range nums {
		if diffBit&n == 0 {
			a ^= n
		} else {
			b ^= n
		}
	}
	return []int{a, b}
}
