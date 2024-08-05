package main

import (
	"fmt"
)

func main() {
	res := kthDistinct([]string{"d", "b", "c", "b", "c", "a"}, 2)
	fmt.Printf("the result is %v", res)
}
