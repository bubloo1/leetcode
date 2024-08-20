package main

import (
	"fmt"
	"go/leetcode/dp"
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
	res := dp.LengthOfLIS([]int{10, 9, 2, 5, 3, 7, 101, 18})
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
