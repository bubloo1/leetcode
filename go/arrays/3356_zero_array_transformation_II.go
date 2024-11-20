package arrays

func MinZeroArray(nums []int, queries [][]int) int {
	temp := make([]int, len(nums)+1)
	use := 0
	sum := 0

	for i, num := range nums {
		sum += temp[i]

		for num-sum > 0 {
			if use == len(queries) {
				return -1
			}

			query := queries[use]
			use++

			if i > query[1] {
				continue
			}

			if i >= query[0] {
				sum += query[2]
			} else {
				temp[query[0]] += query[2]
			}

			if query[1]+1 < len(temp) {
				temp[query[1]+1] -= query[2]
			}
		}
	}

	return use
}
