class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers) - 1

        while s < e:
            currSum = numbers[s] + numbers[e]

            if currSum > target:
                e -= 1
            elif currSum < target:
                s += 1
            else:
                return [s+ 1, e+1]
