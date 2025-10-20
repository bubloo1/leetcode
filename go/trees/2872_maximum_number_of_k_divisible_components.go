package trees

func MaxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {

	// Create adjacency list
	graph := make([][]int, n)
	for _, edge := range edges {
		u, v := edge[0], edge[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	// Calculate subtree sums using DFS
	subtreeSums := make([]int, n)
	var dfs func(node, parent int) int
	dfs = func(node, parent int) int {
		subtreeSum := values[node]
		for _, neighbor := range graph[node] {
			if neighbor != parent {
				subtreeSum += dfs(neighbor, node)
			}
		}
		subtreeSums[node] = subtreeSum
		return subtreeSum
	}
	dfs(0, -1)

	// Count k-divisible components
	count := 0
	for _, sum := range subtreeSums {
		if sum%k == 0 {
			count++
		}
	}

	return count
}
