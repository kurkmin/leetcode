class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # brute force solution 
        # square first 
        # then use python's built-in function 
        for i in range(len(nums)):
            nums[i] *= nums[i] 
        nums.sort() 
        return nums 
            
        
         