package arrays

import (
	"fmt"
	"strconv"
	"time"
)

func Count() {
	for i := 0; i <= 10; i++ {
		fmt.Printf("the number is : %d\n", i)
		time.Sleep(1 * time.Second)
	}

}
func Count2() {
	for ch := 'A'; ch <= 'Z'; ch++ {
		fmt.Printf("the char is : %c\n", ch)
		time.Sleep(1 * time.Second)
	}

}

func ConversStrinToNumber(num string) int {
	ans, _ := strconv.Atoi(num)
	return ans
}

// type shape interface {
// 	area() float64
// }

// type circle struct {
// 	radius float64
// }

// type rect struct {
// 	width  float64
// 	height float64
// }

// func (r rect) area() float64 {
// 	return r.width * r.height
// }

// func (c circle) area() float64 {
// 	return math.Pi * c.radius * c.radius
// }

// func main() {
// 	c1 := circle{4.5}
// 	r1 := rect{5, 7}
// 	shapes := []shape{r1, c1}
// 	for _, shape := range shapes {
// 		fmt.Println(shape.area())
// 	}
// }

///////////// contest 144 //////////

// func CanAliceWin(n int) bool {
// 	currStones := 10
// 	hasAliceWon := false
// 	for currStones <= n {
// 		n -= currStones
// 		currStones--
// 		hasAliceWon = !hasAliceWon
// 	}

// 	return hasAliceWon
// }

// func ShiftDistance(s string, t string, nextCost []int, previousCost []int) int64 {
// cost := 0
// for i := range s {
// 	currSChar := s[i] - 'a'
// 	currTChar := t[i] - 'a'

// 	if s[i] == t[i] {
// 		continue
// 	} else if nextCost[currChar] <= previousCost[currChar] {
// 		cost += nextCost[currChar] * int(t[i]-s[i])
// 		fmt.Println(int(t[i]-s[i]), "next")
// 		currChar++
// 	} else {
// 		cost += previousCost[currChar] * int(t[i]-s[i])
// 		fmt.Println(int(t[i]-s[i]), "prev")
// 		currChar--
// 	}
// }

// 	return int64(12)
// }
