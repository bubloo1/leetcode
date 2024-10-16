package main

import (
	"fmt"
	"go/leetcode/bitmap"
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
	res := bitmap.SingleNumber([]int{1, 2, 1, 3, 2, 5})
	fmt.Printf("the result is %v", res)

}
