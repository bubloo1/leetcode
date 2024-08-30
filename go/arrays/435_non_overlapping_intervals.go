package arrays

import (
	"sort"
)

func EraseOverlapIntervals(intervals [][]int) int {

	const start = 0
	res := 0
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][start] < intervals[j][start]
	})
	currInterval := []int{intervals[0][0], intervals[0][1]}
	for i := 1; i < len(intervals); i++ {
		if currInterval[1] <= intervals[i][0] {
			currInterval = intervals[i]
		} else {
			res++
			currInterval = []int{currInterval[0], min(intervals[i][1], currInterval[1])}
		}
	}
	return res
}
