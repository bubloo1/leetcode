package arrays

import "unicode"

func calculate(s string) int {
	number := 0
	signValue := 1
	result := 0
	stack := []int{}

	for _, c := range s {
		if unicode.IsDigit(c) {
			number = number*10 + int(c-'0')
		} else if c == '+' || c == '-' {
			result += number * signValue
			if c == '-' {
				signValue = -1
			} else {
				signValue = 1
			}
			number = 0
		} else if c == '(' {
			stack = append(stack, result)
			stack = append(stack, signValue)
			result = 0
			signValue = 1
		} else if c == ')' {
			result += signValue * number
			result *= stack[len(stack)-1]
			result += stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			number = 0
		}
	}

	return result + number*signValue
}
