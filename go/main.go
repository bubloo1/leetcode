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
	// root := &trees.TreeNode{Val: 3}
	// root.Left = &trees.TreeNode{Val: 1}
	// root.Right = &trees.TreeNode{Val: 4}
	// root.Right.Left = &trees.TreeNode{Val: 2}

	res := arrays.LargestAltitude([]int{-4, -3, -2, -1, 4, 3, 2})
	fmt.Printf("the result is %v", res)

}
