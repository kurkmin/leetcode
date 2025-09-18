class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        currSum = sum(nums[:k])
        currMax = currSum
        for right in range(k, len(nums)):
            currSum = currSum - nums[left] + nums[right]
            if currSum > currMax:
                currMax = currSum
            left += 1
        return currMax / k
