package main

import (
	"fmt"
)

// type userDetails struct {
// 	name   string
// 	age    int16
// 	gender string
// }

func main() {
	// root := &TreeNode{Val: 5}
	// root.Left = &TreeNode{Val: 1}
	// root.Right = &TreeNode{Val: 4}
	// root.Right.Left = &TreeNode{Val: 3}
	// root.Right.Right = &TreeNode{Val: 6}
	res := calculate("(1+(4+5+2)-3)+(6+8)")
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
