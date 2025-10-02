class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # position of non-zero element
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1

        """
        Do not return anything, modify nums in-place instead.
        """
