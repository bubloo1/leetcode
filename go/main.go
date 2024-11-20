package main

import (
	"fmt"
	"go/leetcode/arrays"
)

func main() {

	// var wg sync.WaitGroup
	// wg.Add(2)

	// go func() {
	// 	defer wg.Done() // Decrement the counter when the Goroutine completes
	// 	arrays.Count()  // Call the first function
	// }()

	// go func() {
	// 	defer wg.Done() // Decrement the counter when the Goroutine completes
	// 	arrays.Count2() // Call the second function
	// }()

	// wg.Wait()
	res := arrays.MinZeroArray([]int{2, 0, 2}, [][]int{{0, 2, 1}, {0, 2, 1}, {1, 1, 3}})
	fmt.Printf("the result is %v", res)

}
