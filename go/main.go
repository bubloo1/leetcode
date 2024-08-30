package main

import (
	"fmt"
	"go/leetcode/arrays"
)

// type userDetails struct {
// 	name   string
// 	age    int16
// 	gender string
// }

func main() {
	// root := &TreeNode{Val: 3}
	// root.Left = &TreeNode{Val: 9}
	// root.Right = &TreeNode{Val: 20}
	// root.Right.Left = &TreeNode{Val: 15}
	// root.Right.Right = &TreeNode{Val: 7}
	// res := dp.IsInterleave("aabcc", "dbbca", "aadbbcbcac")
	res := arrays.PlusOne([]int{7, 2, 8, 5, 0, 9, 1, 2, 9, 5, 3, 6, 6, 7, 3, 2, 8, 4, 3, 7, 9, 5, 7, 7, 4, 7, 4, 9, 4, 7, 0, 1, 1, 1, 7, 4, 0, 0, 6})
	fmt.Printf("the result is %v", res)
	// var user = userDetails{
	// 	name:   "bubloo",
	// 	age:    24,
	// 	gender: "male",
	// }

	// var res userDetails = returnUserDetails(user)
	// fmt.Println(res)
	// fmt.Println(userDetails.formatUserDetails(user))
}

// func returnUserDetails(user userDetails) userDetails {
// 	return user
// }

// func (details userDetails) formatUserDetails() string {
// 	return "the user name is" + details.name
// }
