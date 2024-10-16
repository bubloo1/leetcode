package bitmap

func MinBitFlips(start int, goal int) int {
	res := start ^ goal
	count := 0
	for res != 0 {
		if res%2 == 1 {
			count++
		}
		res = res >> 1
	}
	return count
}
