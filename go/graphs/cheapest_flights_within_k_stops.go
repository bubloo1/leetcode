package graphs

import (
	"math"
)

func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int {

	var adjList = make(map[int][][2]int)

	for _, flight := range flights {
		var src, dst, price = flight[0], flight[1], flight[2]
		adjList[src] = append(adjList[src], [2]int{dst, price})
	}

	var dist = make([]int, n)
	for i := range dist {
		dist[i] = math.MaxInt32
	}

	dist[src] = 0
	var queue = [][3]int{{0, src, 0}}

	for len(queue) > 0 {

		var stops, node, cost = queue[0][0], queue[0][1], queue[0][2]
		queue = queue[1:]

		if stops > k {
			continue
		}

		for _, neigbour := range adjList[node] {
			var adjNode, newCost = neigbour[0], neigbour[1]

			if newCost+cost < dist[adjNode] && stops <= k {

				dist[adjNode] = newCost + cost
				queue = append(queue, [3]int{stops + 1, adjNode, cost + newCost})
			}
		}
	}
	if dist[dst] == math.MaxInt32 {
		return -1
	}
	return dist[dst]
}
