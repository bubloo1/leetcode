package main

func canBeEqual(target []int, arr []int) bool {
	var targetSet = make(map[int]int, len(arr))

	for _, v := range target {
		if _, exists := targetSet[v]; !exists {
			targetSet[v] = 1
		} else {
			targetSet[v] += 1
		}
	}

	for _, v := range arr {
		if _, exists := targetSet[v]; !exists {
			return false
		}
		targetSet[v] -= 1
		if targetSet[v] == 0 {
			delete(targetSet, v)
		}

	}
	return true
}
