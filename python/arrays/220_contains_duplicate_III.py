from sortedcontainers import SortedSet
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        if k <= 0 or t < 0:
            return False

        sorted_window = SortedList()

        for i in range(len(nums)):
            # Maintain a window of size k
            if i > k:
                sorted_window.remove(nums[i - k - 1])

            # Calculate lower and upper bounds
            lower_bound = nums[i] - t
            upper_bound = nums[i] + t

            # Check if there's any number in the sorted list that satisfies the condition
            # We can find a range [lower_bound, upper_bound]
            pos = sorted_window.bisect_left(lower_bound)

            # Check if the found position is within bounds and the value is within upper_bound
            if pos < len(sorted_window) and sorted_window[pos] <= upper_bound:
                return True

            # Add the current number to the sorted list
            sorted_window.add(nums[i])

        return False

# Example usage
nums = [1, 5, 9, 1, 5, 9]
k = 2
t = 3
newObject = Solution()
res = newObject.containsNearbyAlmostDuplicate(nums, k, t)
print("Contains nearby almost duplicate:", res)  # Output: False
