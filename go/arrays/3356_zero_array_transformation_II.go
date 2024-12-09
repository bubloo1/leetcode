package arrays

func MinZeroArray(nums []int, queries [][]int) int {
	n := len(nums)

	// Function to check if the first `m` queries can satisfy the condition
	check := func(m int) bool {
		arr := make([]int, n+1)
		for i := 0; i < m; i++ {
			start, end, val := queries[i][0], queries[i][1], queries[i][2]
			arr[start] += val
			if end+1 < len(arr) {
				arr[end+1] -= val
			}
		}

		cur := 0
		for i := 0; i < n; i++ {
			cur += arr[i]
			if cur < nums[i] {
				return false
			}
		}
		return true
	}

	// If all queries cannot satisfy the array, return -1
	if !check(len(queries)) {
		return -1
	}

	// Binary search to find the minimum number of queries
	l, r := 0, len(queries)
	for l <= r {
		m := l + (r-l)/2
		if check(m) {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	return l

	// temp := make([]int, len(nums)+1)
	// use := 0
	// sum := 0

	// for i, num := range nums {
	// 	sum += temp[i]

	// 	for num-sum > 0 {
	// 		if use == len(queries) {
	// 			return -1
	// 		}

	// 		query := queries[use]
	// 		use++

	// 		if i > query[1] {
	// 			continue
	// 		}

	// 		if i >= query[0] {
	// 			sum += query[2]
	// 		} else {
	// 			temp[query[0]] += query[2]
	// 		}

	// 		if query[1]+1 < len(temp) {
	// 			temp[query[1]+1] -= query[2]
	// 		}
	// 	}
	// }

	// return use
}
