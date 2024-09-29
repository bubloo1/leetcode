package arrays

import "fmt"

func Multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}

	n1 := num1
	n2 := num2
	result := make([]byte, len(num1)+len(num2))
	for i := len(n1) - 1; i >= 0; i-- {
		for j := len(n2) - 1; j >= 0; j-- {
			v1 := n1[i] - '0'
			v2 := n2[j] - '0'
			result[i+j+1] += (v1 * v2)
			fmt.Printf("the result %v", result)
			if result[i+j+1] >= 10 {
				result[i+j] += (result[i+j+1] / 10)
				result[i+j+1] %= 10
			}
		}
	}
	fmt.Printf("the result %v", result)
	if result[0] == 0 {
		result = result[1:]
	}

	for i := range result {
		result[i] += '0'
	}

	return string(result)
}
