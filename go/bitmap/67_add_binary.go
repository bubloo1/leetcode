package bitmap

func addBinary(a string, b string) string {
	i, j := len(a)-1, len(b)-1
	carry := 0
	result := ""

	for i >= 0 || j >= 0 || carry > 0 {
		bit1 := 0
		if i >= 0 {
			bit1 = int(a[i] - '0')
			i--
		}

		bit2 := 0
		if j >= 0 {
			bit2 = int(b[j] - '0')
			j--
		}

		// Calculate the sum of bits and the carry
		sum := bit1 + bit2 + carry
		result = string(sum%2+'0') + result // Append the current bit to the result
		carry = sum / 2                     // Update the carry
	}

	return result

}
