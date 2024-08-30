package arrays

import "sort"

func Merge(intervals [][]int) [][]int {
	res := [][]int{}
	const start = 0
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][start] < intervals[j][start]
	})
	for i := 0; i < len(intervals); i++ {
		if len(res) >= 1 && res[len(res)-1][1] >= intervals[i][0] {
			res[len(res)-1][1] = max(intervals[i][1], res[len(res)-1][1])
		} else {
			res = append(res, intervals[i])
		}
	}
	return res
}
