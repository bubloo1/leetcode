
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # Perform binary search to find the closest element or the potential insertion point
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
      
        # Initialize pointers around the closest element to x
        left, right = left - 1, left

        # Expand around the closest element to find k elements
        while k > 0:
            if left < 0:
                right += 1
            elif right >= len(arr) or (x - arr[left] <= arr[right] - x):
                left -= 1
            else:
                right += 1
            k -= 1

        # Return the result within the range [left + 1, right)
        return arr[left + 1:right]

        # left, right = 0, len(arr) - k  # We only need to consider windows of size k
        
        # # Binary search for the best left boundary of the sliding window
        # while left < right:
        #     mid = (left + right) // 2
        #     # Compare the distance between x and the middle element and the k-th element from mid
        #     if x - arr[mid] > arr[mid + k] - x:
        #         left = mid + 1
        #     else:
        #         right = mid
        
        # # Return the k elements from the left boundary
        # return arr[left:left + k]




newObject = Solution()
print(newObject.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3)) 





        # left, right = 0, len(arr) - k  # We only need to consider windows of size k
        
        # # Binary search for the best left boundary of the sliding window
        # while left < right:
        #     mid = (left + right) // 2
        #     # Compare the distance between x and the middle element and the k-th element from mid
        #     if x - arr[mid] > arr[mid + k] - x:
        #         left = mid + 1
        #     else:
        #         right = mid
        
        # # Return the k elements from the left boundary
        # return arr[left:left + k]
    
print(1//2)