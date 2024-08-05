package main

func kthDistinct(arr []string, k int) string {

	var stringMap = make(map[string]int, len(arr))

	for _, ele := range arr {
		if _, exists := stringMap[ele]; !exists {
			stringMap[ele] = 1
		} else {
			stringMap[ele] += 1
		}
	}

	for _, ele := range arr {
		if stringMap[ele] == 1 {
			k--
		}
		if k == 0 {
			return ele
		}
	}

	return ""
}
