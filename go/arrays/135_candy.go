package arrays

func Candy(ratings []int) int {
	res := make([]int, len(ratings))

	for i := range res {
		res[i] = 1
	}

	for i := 1; i < len(ratings); i++ {
		if ratings[i-1] < ratings[i] {
			res[i] = res[i-1] + 1
		}
	}

	for j := len(ratings) - 2; j >= 0; j-- {
		if ratings[j] > ratings[j+1] {
			res[j] = max(res[j], res[j+1]+1)
		}
	}

	return findSum(res)
}

func findSum(res []int) int {
	ans := 0
	for i := range res {
		ans += res[i]
	}
	return ans
}
