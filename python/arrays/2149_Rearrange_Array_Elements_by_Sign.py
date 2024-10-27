class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # positive_hashmap = []
        # negative_hashmap = []

        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         positive_hashmap.append(nums[i])
        #     elif nums[i] < 0:
        #         negative_hashmap.append(nums[i])
        # res = []
        # for i in range(len(nums)//2):
        #     res.append(positive_hashmap.pop(0))
        #     res.append(negative_hashmap.pop(0))
        
        # return res


        positive_number = 0
        negative_number = 1
        res = [0] * len(nums)
      
        for i in range(len(nums)):
            if nums[i] > 0:
                res[positive_number] = nums[i]
                positive_number += 2
            elif nums[i] < 0:
                res[negative_number] = nums[i]
                negative_number += 2
        return res
            
 



        