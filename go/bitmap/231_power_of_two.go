package bitmap

func IsPowerOfTwo(n int) bool {

	// n & (n-1) = 1000 & 0111 = 0000 (equals 0)
	// when we subtract 1 from 1000 we loose most significant bit and wll
	// get 0111
	if n <= 0 {
		return false
	}
	return (n & (n - 1)) == 0

	// if n == 1 {
	// 	return true
	// }
	// power := 1
	// for i := 1; i < n; i++ {
	// 	power = power * 2

	// 	if power == n {
	// 		return true
	// 	} else if power > n {
	// 		return false
	// 	}
	// }
	// return false
}
