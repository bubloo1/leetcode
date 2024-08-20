from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        charIndexOfNums1 = {}
        res = [-1] * len(nums1)
        stack = []

        for i,n in enumerate(nums1):
            charIndexOfNums1[n] = i
        
        for i,n in enumerate(nums2):

            while stack and stack[-1] < n:
                prevNum = stack.pop()
                index = charIndexOfNums1[prevNum]
                res[index] = n

            if n in charIndexOfNums1:
                stack.append(n)

        return res


newObject = Solution()

print(newObject.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))