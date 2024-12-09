package arrays

type NumMatrix struct {
	matrix [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	// creating presummatrix and adding matrix values
	preSumMatrix := make([][]int, len(matrix)+1)
	for i := range preSumMatrix {
		preSumMatrix[i] = make([]int, len(matrix[0])+1)
	}

	// cal presum
	for r := 0; r < len(matrix); r++ {
		prefix := 0
		for c := 0; c < len(matrix[0]); c++ {
			prefix += matrix[r][c]
			above := preSumMatrix[r][c+1]
			preSumMatrix[r+1][c+1] = prefix + above
		}
	}

	return NumMatrix{
		matrix: preSumMatrix,
	}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	total := 0

	r1, c1, r2, c2 := row1+1, col1+1, row2+1, col2+1

	topLeft := this.matrix[r1-1][c1-1]
	bottomRight := this.matrix[r2][c2]
	above := this.matrix[r1-1][c2]
	left := this.matrix[r2][c1-1]
	total = bottomRight - above - left + topLeft

	// brute force solution
	// Traverse through the specified sub-matrix
	// for i := row1; i <= row2; i++ {
	// 	for j := col1; j <= col2; j++ {
	// 		total += this.matrix[i][j]
	// 	}
	// }

	return total
}
