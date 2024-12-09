package dp

func UniquePathsWithObstacles(obstacleGrid [][]int) int {
	var backtrack func(down, right int) int

	dp := make([][]int, len(obstacleGrid))
	for i := range dp {
		dp[i] = make([]int, len(obstacleGrid[0]))
	}

	backtrack = func(down, right int) int {

		if down < 0 || right < 0 || obstacleGrid[down][right] == 1 {
			return 0
		}

		if down == 0 && right == 0 {
			return 1
		}

		if dp[down][right] != 0 {
			return dp[down][right]
		}

		dp[down][right] += backtrack(down-1, right) + backtrack(down, right-1)
		return dp[down][right]
	}

	return backtrack(len(obstacleGrid)-1, len(obstacleGrid[0])-1)

}
