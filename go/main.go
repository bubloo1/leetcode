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
	res := arrays.MinSubArrayLen(7, []int{2, 3, 1, 2, 4, 3})
	fmt.Printf("the result is %v", res)

}
