package dp

func beautifulSplits(nums []int) int {
	n := len(nums)
	// Create a 2D slice for the longest match
	longestMatch := make([][]int, n)
	for i := range longestMatch {
		longestMatch[i] = make([]int, n)
	}

	// Compute the longest match table
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if nums[i] != nums[j] {
				continue
			}
			longestMatch[i][j] = 1
			if i > 0 {
				longestMatch[i][j] += longestMatch[i-1][j-1]
			}
		}
	}

	result := 0

	// Check for valid splits
	for i := 1; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			len1 := i
			len2 := j - i
			len3 := n - j
			if (len1 <= len2 && longestMatch[i-1][i-1+len1] == len1) ||
				(len2 <= len3 && longestMatch[j-1][j-1+len2] >= len2) {
				result++
			}
		}
	}

	return result

}

// brute force
// n = len(nums)
// count = 0

// def is_prefix(arr1, arr2):

// 	if len(arr1) > len(arr2):
// 		return False

// 	for k in range(len(arr1)):
// 		if arr1[k] != arr2[k]:
// 			return False

// 	return True

// for i in range(1, n - 1):  # Iterate through possible split points for nums1 and nums2
// 	for j in range(i + 1, n):  # Iterate through possible split points for nums2 and nums3
// 		nums1 = nums[:i]
// 		nums2 = nums[i:j]
// 		nums3 = nums[j:]

// 		if len(nums1) == 0 or len(nums2) == 0 or len(nums3) == 0:
// 			continue

// 		if is_prefix(nums1, nums2) or is_prefix(nums2, nums3):
// 			count += 1

// return count
