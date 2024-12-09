from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Pair nums2 and nums1, then sort by nums2 in descending order
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        max_score = 0
        heap = []  # Min-heap to track the largest `k` elements in nums1
        current_sum = 0

        for num2, num1 in pairs:
            # Add nums1 value to the heap and update the current sum
            heapq.heappush(heap, num1)
            current_sum += num1
            
            # If the heap exceeds size k, remove the smallest element
            if len(heap) > k:
                current_sum -= heapq.heappop(heap)
            
            # If the heap has exactly k elements, calculate the score
            if len(heap) == k:
                max_score = max(max_score, current_sum * num2)
        
        return max_score



newObject = Solution()
print(newObject.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))