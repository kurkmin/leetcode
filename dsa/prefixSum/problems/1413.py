class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Hint: Find the minimum prefix sum 
        prefix = [nums[0]]
        for i in range(1, len(nums)): 
            prefix.append(nums[i] + prefix[-1])
        preMin = min(prefix)
        # the minimum value - prefix minimum = 1 
        minimum = 1 - preMin 
        if minimum <= 0:
            minimum = 1 
        return minimum 
        

        

        