package arrays

func PartitionLabels(s string) []int {
	var charHashMap = make(map[rune]int)

	for i, char := range s {
		charHashMap[char] = i
	}

	end := 0
	var res []int
	size := 0
	for i, char := range s {
		end = max(end, charHashMap[char])
		size++
		if i == end {
			res = append(res, size)
			size = 0
		}
	}

	return res
}
