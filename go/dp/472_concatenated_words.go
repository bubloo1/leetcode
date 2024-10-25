package dp

func FindAllConcatenatedWordsInADict(words []string) []string {

	wordSet := make(map[string]bool)
	for _, word := range words {
		wordSet[word] = true
	}

	dp := make(map[string]bool)

	var canForm func(word string) bool
	canForm = func(word string) bool {

		if val, exists := dp[word]; exists {
			return val
		}

		for i := 1; i < len(word); i++ {
			prefix := word[:i]
			suffix := word[i:]

			if wordSet[prefix] && (wordSet[suffix] || canForm(suffix)) {
				dp[word] = true
				return true
			}
		}

		dp[word] = false
		return false
	}

	result := []string{}

	for _, word := range words {
		if canForm(word) {
			result = append(result, word)
		}
	}

	return result
}
