package recursion

func LastRemaining(n int) int {
	// When the elimination is from the left, the first element is always eliminated.
	// When the elimination is from the right, the first element is eliminated only if the count of remaining numbers is odd.
	// step: Initially set to 1, this represents the gap between the numbers after every elimination round. It doubles after each round since every second number is removed.
	// head: This is the first number remaining in the current round. It is updated when we are eliminating from the left or when eliminating from the right with an odd number of elements left.
	left := true
	step := 1
	remaining := n
	head := 1

	for remaining > 1 {
		if left || remaining%2 == 1 {
			head += step
		}

		remaining /= 2
		step *= 2
		left = !left
	}
	return head
}
