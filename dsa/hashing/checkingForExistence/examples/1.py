class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in myDict:
                return [i, myDict[complement]]
            myDict[num] = i
        return (-1, -1)
