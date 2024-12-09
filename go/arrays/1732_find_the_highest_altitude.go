package arrays

func LargestAltitude(gain []int) int {
	maxAltitude, currAltitude := 0, 0

	for _, val := range gain {
		currAltitude += val
		maxAltitude = max(maxAltitude, currAltitude)
	}
	return maxAltitude
}
