package bitmap

func hammingWeight(n int) int {
	var res int = 0
	for n > 0 {
		res = res + n%2
		n = n >> 1
	}
	return res
}
