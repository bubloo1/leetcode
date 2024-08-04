package main

import (
	"fmt"
)

func main() {
	res := canBeEqual([]int{1, 2, 2, 3}, []int{1, 1, 2, 3})
	fmt.Printf("the result is %t", res)
}
