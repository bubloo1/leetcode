package main

import (
	"fmt"
	"go/leetcode/dp"
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
	res := dp.FindAllConcatenatedWordsInADict([]string{"cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"})
	fmt.Printf("the result is %v", res)

}
