package recursion

import "strconv"

func SplitString(s string) bool {
	// Helper function for DFS
	var dfs func(index int, prev int) bool
	dfs = func(index int, prev int) bool {
		if index == len(s) {
			return true
		}

		for j := index; j < len(s); j++ {
			// Convert substring to integer
			val, _ := strconv.Atoi(s[index : j+1])
			// Check if current value is one less than the previous
			if val+1 == prev && dfs(j+1, val) {
				return true
			}
		}
		return false
	}

	// Iterate over possible starting points
	for i := 0; i < len(s)-1; i++ {
		val, _ := strconv.Atoi(s[:i+1])
		if dfs(i+1, val) {
			return true
		}
	}

	return false
}
