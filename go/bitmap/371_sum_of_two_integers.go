package bitmap

func getSum(a int, b int) int {

	// 1001 9
	// 1011 11

	// 10010 &
	// 0010 ^

	for b != 0 {
		temp := (a & b) << 1
		a = (a ^ b)
		b = temp
	}
	return a
}
