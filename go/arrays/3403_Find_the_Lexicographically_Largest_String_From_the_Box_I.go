package arrays

func answerString(word string, numFriends int) string {
	// If only one friend, return the whole string
	if numFriends == 1 {
		return word
	}

	n := len(word)
	m := n - numFriends + 1
	res := ""

	// Iterate to find the lexicographically largest substring
	for i := 0; i < n; i++ { // Ensure the substring length is valid
		sub := word[i:min(i+m, n)]
		if sub >= res {
			res = sub
		}
	}

	return res
}
