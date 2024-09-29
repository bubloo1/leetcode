package recursion

func SortArray(nums []int) []int {
	// return quickSort(nums, 0, len(nums)-1)
	return mergeSort(nums, 0, len(nums)-1)
}

func mergeSort(nums []int, l, r int) []int {
	if l < r {
		m := (l + r) / 2
		mergeSort(nums, l, m)
		mergeSort(nums, m+1, r)
		merge(nums, l, m, r)
	}
	return nums
}

func merge(nums []int, l, m, r int) {
	left, right := make([]int, m-l+1), make([]int, r-m)
	copy(left, nums[l:m+1])
	copy(right, nums[m+1:r+1])

	i, j, k := l, 0, 0

	for j < len(left) && k < len(right) {
		if left[j] < right[k] {
			nums[i] = left[j]
			j++
		} else {
			nums[i] = right[k]
			k++
		}
		i++
	}

	for j < len(left) {
		nums[i] = left[j]
		i++
		j++
	}
	for k < len(right) {
		nums[i] = right[k]
		i++
		k++
	}
}

// func quickSort(nums []int, low, high int) []int {
// 	if low < high {
// 		// Partition the array and get the pivot index
// 		p := partition(nums, low, high)

// 		// Recursively sort elements before and after the partition
// 		quickSort(nums, low, p-1)
// 		quickSort(nums, p+1, high)
// 	}
// 	return nums
// }

// func partition(nums []int, low, high int) int {
// 	// Choose the last element as the pivot
// 	pivot := nums[high]
// 	i := low - 1

// 	// Rearrange the array by placing elements smaller than the pivot to the left
// 	// and elements greater than the pivot to the right
// 	for j := low; j < high; j++ {
// 		if nums[j] < pivot {
// 			i++
// 			// Swap nums[i] and nums[j]
// 			nums[i], nums[j] = nums[j], nums[i]
// 		}
// 	}

// 	// Place the pivot in its correct position
// 	nums[i+1], nums[high] = nums[high], nums[i+1]

// 	// Return the index of the pivot
// 	return i + 1
// }
