package main

func isUgly(n int) bool {
	if n == 0 {
		return false
	}
	for _, pf := range []int{2, 3, 5} {
		for n%pf == 0 {
			n = n / pf
		}
	}

	if n == 1 {
		return true
	}
	return false
}
