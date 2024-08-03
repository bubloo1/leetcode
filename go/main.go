package main

import (
	"fmt"
)

func main() {
	res := findCheapestPrice(5, [][]int{
		{4, 1, 1},
		{1, 2, 3},
		{0, 3, 2},
		{0, 4, 10},
		{3, 1, 1},
		{1, 4, 3},
	}, 2, 1, 1)
	fmt.Printf("the result is %d", res)
}
