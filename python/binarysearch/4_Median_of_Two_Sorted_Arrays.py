from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # sizeOfNums1 = len(nums1) 
        # sizeOfNums2 = len(nums2) 
        # index1 = (sizeOfNums1 + sizeOfNums2)//2
        # index2 = index1 - 1
        # count = 0
        # left = 0
        # right = 0
    
        # while sizeOfNums1 > left and sizeOfNums2 > right:
        #     if nums1[left] > nums2[right]:
        #         if count == index1: firstElement = nums2[right]
        #         if count == index2: secondElement = nums2[right]
        #         count += 1
        #         right += 1
        #     else:
        #         if count == index1: firstElement = nums1[left]
        #         if count == index2: secondElement = nums1[left]
        #         count += 1
        #         left += 1
    
        # while sizeOfNums1 > left:
        #     if count == index1: firstElement = nums1[left]
        #     if count == index2: secondElement = nums1[left]
        #     count += 1
        #     left += 1
            
            
        # while sizeOfNums2 > right:
        #     if count == index1: firstElement = nums2[right]
        #     if count == index2: secondElement = nums2[right]
        #     count += 1
        #     right += 1
        
    
        # if (sizeOfNums1 + sizeOfNums2) % 2 == 0:
        #     return (firstElement + secondElement)/2
        # else:
        #     return firstElement

        
        lenOfNums1, lenOfNums2 = len(nums1) , len(nums2)

        if lenOfNums1 > lenOfNums2:
            return self.findMedianSortedArrays( nums2, nums1)

        n = lenOfNums1 + lenOfNums2
        left = (n + 1)//2

        low,high = 0, len(nums1) 

        while low <= high:
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')

            mid1 = (low + high) // 2
            mid2 = left - mid1

            if mid1 < lenOfNums1:
                r1 = nums1[mid1]

            if mid2 < lenOfNums2:
                r2 = nums2[mid2]

            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]

            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]            
            

            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

            # eliminate the halves:
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0  # dummy statement

