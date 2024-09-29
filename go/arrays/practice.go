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
