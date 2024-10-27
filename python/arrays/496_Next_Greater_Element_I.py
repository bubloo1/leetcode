from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1Idx = { n:i for i, n in enumerate(nums1) }
        # res = [-1] * len(nums1)
        
        # for i in range(len(nums2)):
        #     if nums2[i] not in nums1Idx:
        #         continue
        #     for j in range(i + 1, len(nums2)):
        #         if nums2[j] > nums2[i]:
        #             idx = nums1Idx[nums2[i]]
        #             res[idx] = nums2[j]
        #             break
        
        # return res

        nums1Idx = {n:i for i,n in enumerate(nums1)}
        res = [-1] * len(nums1) 
        stack = []
        for nums2Idx in range(len(nums2)):
            curr = nums2[nums2Idx]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = curr

            if curr in nums1Idx:
                stack.append(curr)
        return res