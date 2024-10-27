
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k  # We only need to consider windows of size k
        
        # Binary search for the best left boundary of the sliding window
        while left < right:
            mid = (left + right) // 2
            # Compare the distance between x and the middle element and the k-th element from mid
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        # Return the k elements from the left boundary
        return arr[left:left + k]