class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        start = 0
        currSum = 0
        for i in range(len(arr)):
        
            currSum = currSum + arr[i]

            if (i - start + 1) % k == 0 and currSum//k >= threshold:
                count += 1
                currSum -= arr[start]
                start += 1
            
            elif (i - start + 1) % k == 0 and currSum//k < threshold:
                currSum -= arr[start]
                start += 1
                
        return count
        