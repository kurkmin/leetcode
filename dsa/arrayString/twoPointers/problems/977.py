class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 1. brute force solution 
        # square first 
        # then use python's built-in function 
        for i in range(len(nums)):
            nums[i] *= nums[i] 
        nums.sort() 

        # 2. two pointers solution (to be added)
        return nums 
            
        
         