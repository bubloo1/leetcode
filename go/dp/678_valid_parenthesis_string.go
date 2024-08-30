package dp

func CheckValidString(s string) bool {
	dp := make(map[int]map[int]bool, len(s))
	return helper(s, 0, 0, dp)
}

func helper(s string, index int, count int, dp map[int]map[int]bool) bool {
	// Base case: If we've reached the end of the string, check if we have a balanced count
	if index == len(s) {
		return count == 0
	}

	// If the count goes negative, it means we have more ')' than '(' which is invalid
	if count < 0 {
		return false
	}

	if _, exists := dp[index]; !exists {
		dp[index] = make(map[int]bool)
	}

	if val, exists := dp[index][count]; exists {
		return val
	}

	// Process the current character
	if s[index] == '(' {
		dp[index][count] = helper(s, index+1, count+1, dp)
	} else if s[index] == ')' {
		dp[index][count] = helper(s, index+1, count-1, dp)
	} else { // s[index] == '*'
		// Try all possible values for '*'
		dp[index][count] = (helper(s, index+1, count+1, dp) || // Treat '*' as '('
			helper(s, index+1, count-1, dp) || // Treat '*' as ')'
			helper(s, index+1, count, dp)) // Treat '*' as ''
	}
	return dp[index][count]
}
