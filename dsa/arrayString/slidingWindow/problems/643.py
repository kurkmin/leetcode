class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = maxi = curr = 0 
        for right in range(len(nums)): 
            curr += nums[right]
            right += 1 
            if right - left + 1 > k:
                curr -= nums[left]
                left += 1
            maxi = max(maxi, sum(nums[left:right]) / (right - left + 1))
        return maxi 
        